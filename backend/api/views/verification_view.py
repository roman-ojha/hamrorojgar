from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from utils.responseObj import ResponseObj
from api.models import citizen
import requests
import json
from decouple import config
import random


class CitizenVerificationSend(APIView):
    def get(self, request: Request, verification_code: str):
        print(verification_code)
        citizen_res = citizen.Citizen.objects.get(
            verification_code=verification_code)
        print(citizen_res)
        otp = random.randint(1000, 9999)
        payload = json.dumps({
            "originator": "SignOTP",
            "recipient": "+9779823336991",
            "content": "Hello this is from Hamrorojgar, your Registration verification code is: {}",
            "expiry": "600",
            "data_coding": "text"
        })
        headers = {
            'Authorization': config("D7_AUTHENTICATION"),
            'Content-Type': 'application/json'
        }
        # print(payload)
        # response = requests.request("POST", config(
        #     "D7_VERIFICATION_OTP_BASE_URL") + "/send-otp", headers=headers, data=payload)
        # print(response.text)
        return Response(ResponseObj(msg="Successfully send otp to your mobile number").get())
