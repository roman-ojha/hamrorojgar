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
from api.models import job_application
import requests
from api.serializers.payment_serializer import PaymentSerializer
from api.models.payment import Payment as PaymentModel
from api.models.payment_gateway import PaymentGateway


class Payment(APIView):
    authentication_classes = [CustomTokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request: Request, payment_gateway: str):
        job_application_id = request.query_params.get('job_application_id')
        # print(payment_gateway)
        # print(job_application_id)
        # print(request.user)
        amount = 2000
        try:
            job_application = job_application.JobApplication.objects.get(
                id=job_application_id)
            if payment_gateway != "khalti":
                return Response(ResponseObj(msg="Invalid request").get(), status=status.HTTP_400_BAD_REQUEST)
            payment_gateway = PaymentGateway.objects.get(code=payment_gateway)
            requestHeader = {"Authorization": config("KHALTI_LIVE_SECRET_KEY")}
            requestParameters = {
                "return_url": config("API_BASE_URL") + "/payment/success",
                "website_url": config("API_BASE_URL"),
                "amount": amount,
                "purchase_order_id": f"HAMROROJGAR-{payment_gateway}-{job_application_id}-{request.user.id}",
                "purchase_order_name": f"job application payment",
            }
            # print(requestHeader, requestParameters)
            # request to khalti to initiate the payment
            response = requests.post(
                config("KHALTI_PAYMENT_BASE_URL") + "/epayment/initiate/", headers=requestHeader, data=requestParameters)
            if response.status_code == 200:
                # save payment into payment table
                payment_serializer = PaymentSerializer(data={
                    'amount': amount, 'payment_using': payment_gateway.id, 'from_acc': None, 'status': PaymentModel.StatusChoices.PENDING,
                    'payment_id': None, 'transaction_id': None, 'by': request.user.pk, 'for_application': job_application.pk
                })
                if payment_serializer.is_valid():
                    print(payment_serializer.validated_data)
                    # payment_serializer.save()
                    return Response(ResponseObj({'pidx': response.json().get('pidx'), 'payment_url': response.json().get('payment_url')}, msg="Successful").get(), status=status.HTTP_400_BAD_REQUEST)
                else:
                    print(payment_serializer.errors)
                    return Response(ResponseObj(msg="Internal server error").get(), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response(ResponseObj(msg="Some error occur trying do payment").get(), status=status.HTTP_400_BAD_REQUEST)
        return Response(ResponseObj(msg="Internal server error").get(), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class PaymentSuccess(APIView):
    def get(self, request: Request, payment_gateway: str):
        print(request.query_params)
        return HttpResponseRedirect(config("CLIENT_BASE_URL") + "/jobs")
