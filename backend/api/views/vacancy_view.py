from rest_framework.views import APIView
from rest_framework.request import Request
from api.models import Vacancy
from api.serializers import VacancySerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class VacancyView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request: Request):
        vacancies = Vacancy.objects.all()
        serialized = VacancySerializer(vacancies, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)
