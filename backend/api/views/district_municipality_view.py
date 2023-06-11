from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from api.models import district
from api.serializers import district_serializer
from rest_framework import status


class District(APIView):
    def get(self, request: Request):
        districts = district.District.objects.all()
        serialized = district_serializer.DistrictSerializer(
            districts, many=True)
        return Response(serialized.data)
