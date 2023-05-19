from rest_framework.serializers import ModelSerializer
from api.models import Qualification


class VacancySerializer(ModelSerializer):
    class Meta:
        model = Qualification
        fields = ['description']
