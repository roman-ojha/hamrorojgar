from django.http import HttpRequest, JsonResponse, HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from api.models import Citizen
from api.serializers import CitizenSerializer
import io
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.views import APIView
from utils.responseObj import ResponseObj
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated


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
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request: Request, pk=None, format=None):
        citizen = Citizen.objects.all()
        serialized = CitizenSerializer(citizen, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def post(self, request: Request, format=None):
        json_data = request.body
        stream = io.BytesIO(json_data)
        py_data = JSONParser().parse(stream=stream)
        serialized_data = CitizenSerializer(data=py_data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(ResponseObj(msg="Registered Citizen User").get(), status=status.HTTP_201_CREATED)
        else:
            return Response(serialized_data.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


class Registration(APIView):
    def post(self, request: Request, format=None):
        json_data = request.body
        stream = io.BytesIO(json_data)
        py_data = JSONParser().parse(stream=stream)
        serialized_data = CitizenSerializer(data=py_data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(ResponseObj(msg="Registered Citizen User").get(), status=status.HTTP_201_CREATED)
        else:
            return Response(serialized_data.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


class Login(APIView):
    pass
