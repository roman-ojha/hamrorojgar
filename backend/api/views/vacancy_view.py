from rest_framework.views import APIView
from rest_framework.request import Request
from api.models import Vacancy
from api.serializers import VacancySerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class VacancyView(APIView):
    def get(self, request: Request):
        id = request.query_params.get('id')
        if (id is None):
            jobs = Vacancy.objects.all()
            serialized = VacancySerializer(jobs, many=True)
            return Response(serialized.data, status=status.HTTP_200_OK)
        jobs = Vacancy.objects.get(id=id)
        serialized = VacancySerializer(jobs)
        return Response(serialized.data, status=status.HTTP_200_OK)
