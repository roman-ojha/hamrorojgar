from rest_framework.serializers import ModelSerializer
from api.models import GovernmentUser, Government


class GovernmentUserSerializer(ModelSerializer):
    class Meta:
        model = GovernmentUser
        fields = ['id', 'email',]


class GovernmentSerializer(ModelSerializer):
    user = GovernmentUserSerializer()

    class Meta:
        model = Government
        fields = ['gov_type', 'user']
