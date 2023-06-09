from rest_framework.serializers import ModelSerializer
from api.models import government
from api.serializers.address_serializer import AddressSerializer


class GovernmentUserSerializer(ModelSerializer):
    class Meta:
        model = government.GovernmentUser
        fields = ['id', 'email',]


class GovernmentSerializer(ModelSerializer):
    user = GovernmentUserSerializer()
    location = AddressSerializer()

    class Meta:
        model = government.Government
        fields = ['gov_type', 'user', 'location']
