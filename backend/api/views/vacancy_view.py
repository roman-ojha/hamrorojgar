from rest_framework.views import APIView
from rest_framework.request import Request
from api.models import Vacancy
from api.serializers import VacancySerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from utils.responseObj import ResponseObj
from rest_framework.parsers import MultiPartParser
import os
from rest_framework.settings import settings


class VacancyView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request: Request):
        vacancies = Vacancy.objects.all()
        serialized = VacancySerializer(vacancies, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)


class ApplyView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request: Request, format=None):
        file_obj = request.FILES.get('file')
        file_path = os.path.join(
            settings.BASE_DIR, "static", "upload", file_obj.name)
        folder_path = os.path.dirname(file_path)
        # create folder if doesn't exist
        os.makedirs(folder_path, exist_ok=True)
        with open(file_path, 'wb') as f:
            for chunk in file_obj.chunks():
                f.write(chunk)
        return Response(ResponseObj(msg="File uploaded successfully").get(), status=status.HTTP_201_CREATED)
