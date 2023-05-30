from django.http import HttpRequest, JsonResponse, HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from api.models import CitizenUser, Citizen
from api.serializers import CitizenSerializer, LoginAuthTokenSerializer, GetCitizenSerializer
import io
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


# # Function Based
# from rest_framework.decorators import api_view
# @api_view(['GET', 'POST'])
# def citizen(request: Request):
#     if request.method == "GET":
#         citizen = Citizen.objects.all()
#         serialized = CitizenSerializer(citizen, many=True)
#         return Response(serialized.data, status=status.HTTP_200_OK)
#     elif request.method == "POST":
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         py_data = JSONParser().parse(stream=stream)
#         serialized_data = CitizenSerializer(data=py_data)
#         if serialized_data.is_valid():
#             serialized_data.save()
#             res = {
#                 'status': True,
#                 'msg': "Registered Citizen User"
#             }
#             return Response(res, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serialized_data.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

class CitizenView(APIView):
    authentication_classes = [CustomTokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request: Request, pk=None, format=None):
        try:
            user = CitizenUser.objects.get(pk=request.user.id)
            citizen = Citizen.objects.get(user=user)
            citizen_serialized = GetCitizenSerializer(citizen)
            return Response(citizen_serialized.data, status=status.HTTP_200_OK)
        except:
            return Response(ResponseObj(msg=constants.HTTP_500_STATUS_MSG).get(), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request: Request, format=None):
        try:
            data_str = request.data.get('json')
            data_dict = json.loads(data_str)
            serialized_data = CitizenSerializer(data={
                **data_dict,
                'photo': request.FILES.get('photo')
            })
            if serialized_data.is_valid():
                print(serialized_data.validated_data)
                serialized_data.save()
                return Response(ResponseObj(msg="Registered Citizen User").get(), status=status.HTTP_201_CREATED)
            else:
                return Response(serialized_data.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
        except:
            return Response(ResponseObj(msg=constants.HTTP_500_STATUS_MSG).get(), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class Registration(APIView):
    def post(self, request: Request, format=None):
        data_str = request.data.get('json')
        data_dict = json.loads(data_str)
        serialized_data = CitizenSerializer(data={
            **data_dict,
            'photo': request.FILES.get('photo')
        })
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(ResponseObj(msg="Registered Citizen User").get(), status=status.HTTP_201_CREATED)
        else:
            return Response(serialized_data.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


class Login(ObtainAuthToken):
    serializer_class = LoginAuthTokenSerializer

    def post(self, request: Request, *args, **kwargs):
        try:
            serialized_data = self.serializer_class(
                data=request.data, context={'request': request})
            if serialized_data.is_valid(raise_exception=True):
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
            return Response(ResponseObj(msg="Invalid Credentials").get(), status=status.HTTP_406_NOT_ACCEPTABLE)
        except citizen.DoesNotExist:
            return Response(ResponseObj(msg="Invalid Credentials").get(), status=status.HTTP_406_NOT_ACCEPTABLE)
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
