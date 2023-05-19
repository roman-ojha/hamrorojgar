from rest_framework import serializers
from django.db import models
from api.models import Citizen, CitizenUser


class CitizenUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CitizenUser
        fields = ['id', 'email', 'password']


class CitizenSerializer(serializers.ModelSerializer):
    user = CitizenUserSerializer()

    class Meta:
        model = Citizen
        fields = ['user', 'f_name', 'm_name', 'l_name', 'mobile', 'date_of_birth',
                  'gender', 'nationality', 'citizenship_no', 'photo_url']
