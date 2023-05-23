from rest_framework.serializers import ModelSerializer
from api.models import Qualification


class QualificationSerializer(ModelSerializer):
    class Meta:
        model = Qualification
        fields = ['id', 'description']
