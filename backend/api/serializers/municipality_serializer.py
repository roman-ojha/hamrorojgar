from rest_framework import serializers
from api.models import municipality


class MunicipalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = municipality.Municipality
        fields = ['id', 'name', 'get_type_label']
