from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from utils.responseObj import ResponseObj
from api.models import citizen
import requests
import json
from decouple import config
from rest_framework import status


# Bellow two view contain verification using SMS OTP

# class CitizenVerificationSend(APIView):
#     def get(self, request: Request, verification_code: str):
#         # try:
#         citizen_res = citizen.Citizen.objects.get(
#             verification_code=verification_code)
#         if citizen_res.is_valid_number == True:
#             return Response(ResponseObj(msg="You are already verified user").get())
#         payload = json.dumps({
#             "originator": "SignOTP",
#             "recipient": "+9779823336991",
#             "content": "Hello this is from Hamrorojgar, your Registration verification code is: {}",
#             "expiry": "600",
#             "data_coding": "text"
#         })
#         headers = {
#             'Content-Type': 'application/json',
#             'Token': config("D7_AUTH_TOKEN"),
#             'X-RapidAPI-Key': '7dec355197msh7d9e8950290b2c0p1975bdjsn68eb69171766',
#             'X-RapidAPI-Host': 'd7-verify.p.rapidapi.com'
#         }
#         response = requests.request("POST", config(
#             "D7_VERIFICATION_OTP_BASE_URL") + "/send-otp", headers=headers, data=payload)
#         print(response.status_code)
#         print(response.json())
#         citizen_res.d7_otp_id = response.json().get('otp_id')
#         citizen_res.save()
#         return Response(ResponseObj(msg="Successfully send otp to your mobile number").get())
#         # except:
#         #     return Response(ResponseObj(msg="Something went wrong, please try again later...").get(), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# class CitizenVerificationReSend(APIView):
#     def get(self, request: Request, verification_code: str):
#         print(verification_code)
#         citizen_res = citizen.Citizen.objects.get(
#             verification_code=verification_code)
#         print(citizen_res)
#         payload = json.dumps({
#             "originator": "SignOTP",
#             "recipient": "+9779823336991",
#             "content": "Hello this is from Hamrorojgar, your Registration verification code is: {}",
#             "expiry": "600",
#             "data_coding": "text"
#         })
#         headers = {
#             'Authorization': config("D7_AUTHENTICATION"),
#             'Content-Type': 'application/json'
#         }
#         # print(payload)
#         # response = requests.request("POST", config(
#         #     "D7_VERIFICATION_OTP_BASE_URL") + "/resend-otp", headers=headers, data=payload)
#         # print(response)
#         return Response(ResponseObj(msg="Successfully send otp to your mobile number").get())
