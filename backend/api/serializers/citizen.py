from rest_framework import serializers
from django.db import models
from api.models import CitizenUser


class CitizenSerializer(serializers.Serializer):
    # user = models.OneToOneField(
    #     CitizenUser, on_delete=models.CASCADE, related_name='citizen')
    f_name = serializers.CharField(max_length=30)
    m_name = serializers.CharField(max_length=30)
    l_name = serializers.CharField(max_length=30)
    mobile = serializers.IntegerField()
    date_of_birth = serializers.DateField()
    gender = serializers.CharField(max_length=3)
    nationality = serializers.CharField(max_length=80)
    citizenship_no = serializers.CharField(max_length=200)
    photo_url = serializers.TextField(max_length=100)
