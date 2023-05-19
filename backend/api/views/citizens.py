from django.http import HttpRequest, JsonResponse, HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from api.models import Citizen
from api.serializers import CitizenSerializer
import io
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def citizen(request: HttpRequest):
    if request.method == "GET":
        citizen = Citizen.objects.all()
        serialized = CitizenSerializer(citizen, many=True)
        return JsonResponse(serialized.data, safe=False)
    elif request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        py_data = JSONParser().parse(stream=stream)
        serialized_data = CitizenSerializer(data=py_data)
        if serialized_data.is_valid():
            print("Valid Citizen")
            # serialized_data.save()
            res = {
                'status': True,
                'msg': "Registered Citizen User"
            }
            json_response = JSONRenderer().render(res)
            return HttpResponse(json_response, content_type="application/json")
        else:
            json_response = JSONRenderer().render(serialized_data.errors)
            return HttpResponse(json_response, content_type="application/json")
