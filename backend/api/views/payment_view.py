from rest_framework.views import APIView
from django.http import HttpResponseRedirect
from rest_framework.response import Response
from api.authentication import CustomTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from utils.responseObj import ResponseObj
from rest_framework import status
import requests


class Payment(APIView):
    authentication_classes = [CustomTokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request: Request, payment_gateway: str):
        job_application_id = request.query_params.get('job_application_id')
        print(payment_gateway)
        print(job_application_id)
        print(request.user)
        return Response(ResponseObj(msg="hello").get())
