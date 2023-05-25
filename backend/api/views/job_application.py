from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from api.authentication import CustomTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from utils.responseObj import ResponseObj
from rest_framework.parsers import MultiPartParser
import os
from rest_framework.settings import settings
from api.serializers import JobApplicationSerializer
import json
from api.models import User

# class ApplyView(APIView):
#     parser_classes = [MultiPartParser]
#     def post(self, request: Request, format=None):
#         file_obj = request.FILES.get('file')
#         file_path = os.path.join(
#             settings.BASE_DIR, "static", "upload", file_obj.name)
#         folder_path = os.path.dirname(file_path)
#         # create folder if doesn't exist
#         os.makedirs(folder_path, exist_ok=True)
#         with open(file_path, 'wb') as f:
#             for chunk in file_obj.chunks():
#                 f.write(chunk)
#         return Response(ResponseObj(msg="File uploaded successfully").get(), status=status.HTTP_201_CREATED)


class ApplyView(APIView):
    parser_classes = [MultiPartParser]
    authentication_classes = [CustomTokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request: Request, format=None):
        vacancy_id = request.query_params.get('vacancy_id')
        serializer = JobApplicationSerializer(data={
            'cv': request.FILES.get('cv'),
            'citizen': request.user.id,
            'vacancy': vacancy_id
        })
        if serializer.is_valid():
            serializer.save()
            return Response(ResponseObj(msg="Application form submitted successfully").get(), status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
