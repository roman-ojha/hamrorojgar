from rest_framework import serializers
from django.db import models
from rest_framework.fields import empty
from api.models import Citizen, CitizenUser
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import authenticate


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

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = CitizenUser.objects.create(**user_data)
        validated_data['user'] = user
        return Citizen.objects.create(**validated_data)


class LoginAuthTokenSerializer(AuthTokenSerializer):
    username = None
    email = serializers.EmailField(label=_("Email"), write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        # print(email)
        # print(password)

        if email and password:
            user = authenticate(request=self.context.get('request'),
                                username=email, password=password)
            print(user)
            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "email" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
