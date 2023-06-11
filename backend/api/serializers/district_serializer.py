from rest_framework import serializers
from api.models import district


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = district.District
        fields = ['id', 'name']
