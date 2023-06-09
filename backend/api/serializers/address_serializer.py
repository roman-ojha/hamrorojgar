from rest_framework import serializers
from api.models import address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = address.Address
        fields = ['district', 'municipality', 'ward_no']
