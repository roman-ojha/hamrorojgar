from rest_framework.serializers import ModelSerializer
from api.models import qualification


class QualificationSerializer(ModelSerializer):
    class Meta:
        model = qualification.Qualification
        fields = ['id', 'description']
