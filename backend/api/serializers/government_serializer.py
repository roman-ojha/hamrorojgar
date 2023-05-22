from rest_framework.serializers import ModelSerializer
from api.models import GovernmentUser, Government
from api.serializers.address_serializer import AddressSerializer


class GovernmentUserSerializer(ModelSerializer):
    class Meta:
        model = GovernmentUser
        fields = ['id', 'email',]


class GovernmentSerializer(ModelSerializer):
    user = GovernmentUserSerializer()
    location = AddressSerializer()

    class Meta:
        model = Government
        fields = ['gov_type', 'user', 'location']
