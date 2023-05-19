from django.http import HttpRequest, JsonResponse, HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from api.models import Citizen
from api.serializers import CitizenSerializer
import io
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request


@api_view(['GET', 'POST'])
def citizen(request: Request):
    if request.method == "GET":
        citizen = Citizen.objects.all()
        serialized = CitizenSerializer(citizen, many=True)
        # return JsonResponse(serialized.data, safe=False)
        return Response(serialized.data)
    elif request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        py_data = JSONParser().parse(stream=stream)
        serialized_data = CitizenSerializer(data=py_data)
        if serialized_data.is_valid():
            serialized_data.save()
            res = {
                'status': True,
                'msg': "Registered Citizen User"
            }
            json_response = JSONRenderer().render(res)
            return HttpResponse(json_response, content_type="application/json")
        else:
            json_response = JSONRenderer().render(serialized_data.errors)
            return HttpResponse(json_response, content_type="application/json")
