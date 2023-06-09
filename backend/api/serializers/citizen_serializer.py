from rest_framework import serializers
from django.db import models
from rest_framework.fields import empty
from api.models import citizen
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import authenticate
from .address_serializer import AddressSerializer
from api.models.address import Address
from decouple import config


class CitizenUserSerializer(serializers.ModelSerializer):
    c_password = serializers.CharField()

    class Meta:
        model = citizen.CitizenUser
        fields = ['id', 'email', 'password', 'c_password']

    def validate(self, attrs):
        if attrs['password'] != attrs['c_password']:
            raise serializers.ValidationError({
                "c_password": [
                    "password doesn't match"
                ]
            }
            )
        return super().validate(attrs)


class CitizenSerializer(serializers.ModelSerializer):
    user = CitizenUserSerializer()
    p_address = AddressSerializer()
    t_address = AddressSerializer(allow_null=True)

    class Meta:
        model = citizen.Citizen
        fields = ['user', 'f_name', 'm_name', 'l_name', 'mobile', 'date_of_birth',
                  'gender', 'nationality', 'citizenship_no', 'photo', 'p_address', 't_address']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        print(user_data)
        del user_data['c_password']
        print(user_data)
        user = citizen.CitizenUser.objects.create_user(**user_data)
        validated_data['user'] = user
        p_address_data = validated_data.pop('p_address')
        t_address_data = validated_data.pop('t_address')
        p_address = Address.objects.create(**p_address_data)
        if t_address_data is not None:
            t_address = Address.objects.create(**t_address_data)
            validated_data['t_address'] = t_address
        validated_data['p_address'] = p_address
        return citizen.Citizen.objects.create(**validated_data)


class GetCitizenSerializer(serializers.ModelSerializer):
    class GetCitizenUserSerializer(serializers.ModelSerializer):
        class Meta:
            model = citizen.CitizenUser
            fields = ['id', 'email']
    user = GetCitizenUserSerializer()
    p_address = AddressSerializer()
    t_address = AddressSerializer(allow_null=True)
    photo = serializers.SerializerMethodField()

    class Meta:
        model = citizen.Citizen
        fields = ['user', 'f_name', 'm_name', 'l_name', 'mobile', 'date_of_birth',
                  'gender', 'nationality', 'citizenship_no', 'photo', 'p_address', 't_address']

    def get_photo(self, obj):
        if obj.photo:
            return config("API_BASE_URL") + obj.photo.url
        return None


class LoginAuthTokenSerializer(AuthTokenSerializer):
    username = None
    email = serializers.EmailField(label=_("Email"), write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'),
                                username=email, password=password)
            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = _('Unable to login with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "email" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
