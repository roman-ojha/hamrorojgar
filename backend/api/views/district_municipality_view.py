from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from api.models import district
from api.serializers import district_serializer
from rest_framework import status
from api.models import municipality
from api.serializers import municipality_serializer
from django.core.exceptions import ObjectDoesNotExist


class District(APIView):
    def get(self, request: Request):
        districts = district.District.objects.all()
        serialized_districts = district_serializer.DistrictSerializer(
            districts, many=True)
        return Response(serialized_districts.data)


class Municipality(APIView):
    def get(self, request: Request, district_id):
        try:
            municipalities = municipality.Municipality.objects.filter(
                district=district_id)
            serialized_municipalities = municipality_serializer.MunicipalitySerializer(
                municipalities, many=True)
            return Response(serialized_municipalities.data)
        except ObjectDoesNotExist:
            return Response([])
