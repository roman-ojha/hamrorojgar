from rest_framework import serializers
from api.models import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['district', 'municipality', 'ward_no']
