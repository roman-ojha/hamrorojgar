from rest_framework.views import APIView
from django.http import HttpResponseRedirect
from rest_framework.response import Response
from api.authentication import CustomTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from utils.responseObj import ResponseObj
from rest_framework import status
from decouple import config
import requests


class Payment(APIView):
    authentication_classes = [CustomTokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request: Request, payment_gateway: str):
        job_application_id = request.query_params.get('job_application_id')
        # print(payment_gateway)
        # print(job_application_id)
        # print(request.user)
        if payment_gateway != "khalti":
            return Response(ResponseObj(msg="Invalid request").get(), status=status.HTTP_400_BAD_REQUEST)
        requestHeader = {"Authorization": config("KHALTI_LIVE_SECRET_KEY")}
        requestParameters = {
            "return_url": config("API_BASE_URL") + "/payment/",
            "website_url": config("API_BASE_URL"),
            "amount": 2000,
            "purchase_order_id": f"HAMROROJGAR-{payment_gateway}-{job_application_id}-{request.user.id}",
            "purchase_order_name": f"job application payment",
            "customer_info": {
                # "name": "Ashim Upadhaya",
                # "email": "example@gmail.com",
                "phone": "9800000005"
            },
        }
        # print(requestHeader, requestParameters)
        response = requests.post(
            config("KHALTI_PAYMENT_BASE_URL") + "/epayment/initiate/", headers=requestHeader, data=requestParameters)
        # print(response.json().get('pidx'))
        # print(response.status_code)
        if response.status_code == 200:
            return Response(ResponseObj({'pidx': response.json().get('pidx'), 'payment_url': response.json().get('payment_url')}, msg="Successful").get(), status=status.HTTP_400_BAD_REQUEST)
        return Response(ResponseObj(msg="Internal server error").get(), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class PaymentSuccess(APIView):
    pass
