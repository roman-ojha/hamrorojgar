from django.http import HttpRequest, JsonResponse, HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from api.models.citizen import Citizen, CitizenUser
from api.serializers import CitizenSerializer, LoginAuthTokenSerializer, GetCitizenSerializer
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.views import APIView
from utils.responseObj import ResponseObj
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
import json
from datetime import datetime, timedelta
from api.authentication import CustomTokenAuthentication
from rest_framework.settings import settings
from data.constants import constants
from utils.email import send_html_email
from data.constants import constants
from decouple import config
from maingovdb.models import Citizen as MainDBCitizen


class CitizenRegister(APIView):
    def post(self, request: Request, format=None):
        data_str = request.data.get('json')
        data_dict = json.loads(data_str)
        serialized_data = CitizenSerializer(data={
            **data_dict,
            'photo': request.FILES.get('photo'),
        })
        if serialized_data.is_valid():
            # check whether provided data is a valid nepali citizen or not // for now we will only check for nepali citizen
            if serialized_data.validated_data.get("nationality") != "nepali":
                return Response(ResponseObj(msg="To get register in this platform you have to be a nepali citizen.").get(), status=status.HTTP_401_UNAUTHORIZED)
            is_valid_citizen = MainDBCitizen.objects.filter(
                citizenship_no=serialized_data.validated_data.get("citizenship_no")).first()
            if not is_valid_citizen:
                return Response(ResponseObj(msg="You don't have authorized citizenship no. that is registered on government database, please contact your nearest municipality office.").get(), status=status.HTTP_401_UNAUTHORIZED)
            if is_valid_citizen.mobile != serialized_data.validated_data.get("mobile"):
                return Response(ResponseObj(msg="Provided mobile number is not registered on you same citizenship no. that you used here, please check and try it again...").get(), status=status.HTTP_401_UNAUTHORIZED)
            serialized_data.save()

            # Send mail after registration:
            subject = f"{constants.APPLICATION_NAME} - Verify you email address"
            recipient_list = [
                serialized_data.validated_data.get('user').get('email')]
            send_html_email(subject, "api/verification_email.html", {'application_name': constants.APPLICATION_NAME, 'citizen_name': serialized_data.validated_data.get(
                'f_name'), 'verification_url': f"{config('API_BASE_URL')}/api/citizen/verify/{serialized_data.instance.user.verification_token}"}, recipient_list)
            return Response(ResponseObj(msg="Citizen registered successfully").get(), status=status.HTTP_201_CREATED)
        else:
            return Response(serialized_data.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


class CitizenLogin(ObtainAuthToken):
    serializer_class = LoginAuthTokenSerializer

    def post(self, request: Request, *args, **kwargs):
        try:
            serialized_data = self.serializer_class(
                data=request.data, context={'request': request})
            if serialized_data.is_valid(raise_exception=False):
                user = serialized_data.validated_data['user']
                token, created = Token.objects.get_or_create(user=user)
                user = CitizenUser.objects.get(pk=user.pk)
                citizen = Citizen.objects.get(user=user)
                citizen_serialized = GetCitizenSerializer(citizen)
                cookie_expire_date = 10
                expiration_date = datetime.utcnow() + timedelta(days=cookie_expire_date)
                formatted_expiration_date = expiration_date.strftime(
                    "%a, %d %b %Y %H:%M:%S GMT")
                response = Response(citizen_serialized.data,
                                    status=status.HTTP_202_ACCEPTED)
                response.set_cookie(
                    key=settings.AUTH_COOKIE_NAME, value=f"Token {token.key}", path='/', expires=formatted_expiration_date, secure=True, samesite='None', httponly=True)
                return response
            else:
                return Response(serialized_data.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
        except user.DoesNotExist:
            return Response(ResponseObj(msg="Unable to login with provided credentials.").get(), status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            return Response(ResponseObj(msg=constants.HTTP_500_STATUS_MSG).get(), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CitizenLogout(APIView):
    authentication_classes = [CustomTokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request: Request, pk=None, format=None):
        try:
            response = Response(request.user.email)
            response.delete_cookie(settings.AUTH_COOKIE_NAME)
            return response
        except Exception as e:
            return Response(ResponseObj(msg=constants.HTTP_500_STATUS_MSG).get(), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
