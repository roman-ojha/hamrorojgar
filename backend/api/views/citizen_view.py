from api.models import citizen
from api.serializers import CitizenSerializer, GetCitizenSerializer
import io
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.views import APIView
from utils.responseObj import ResponseObj
from rest_framework.permissions import IsAuthenticated
import json
from api.authentication import CustomTokenAuthentication
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
            user = citizen.CitizenUser.objects.get(pk=request.user.id)
            citizen = citizen.Citizen.objects.get(user=user)
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
