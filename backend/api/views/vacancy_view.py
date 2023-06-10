from rest_framework.views import APIView
from rest_framework.request import Request
from api.models import vacancy
from api.serializers import VacancySerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from data.constants import constants
from utils.responseObj import ResponseObj
from api.algolia import client


class JobListView(APIView):
    def get(self, request: Request):
        try:
            id = request.query_params.get('id')
            if (id is None):
                jobs = vacancy.Vacancy.objects.all()
                serialized = VacancySerializer(jobs, many=True)
                return Response(serialized.data, status=status.HTTP_200_OK)
            jobs = vacancy.Vacancy.objects.get(id=id)
            serialized = VacancySerializer(jobs)
            return Response(serialized.data, status=status.HTTP_200_OK)
        except:
            return Response(ResponseObj(msg=constants.HTTP_500_STATUS_MSG).get(), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SearchJobs(APIView):
    def get(self, request: Request, *args, **kwargs):
        query = request.query_params.get('q')
        if not query:
            return Response(ResponseObj(msg="Could not find query parameter").get(), status=status.HTTP_400_BAD_REQUEST)
        results = client.perform_search(query=query)
        return Response(results)
