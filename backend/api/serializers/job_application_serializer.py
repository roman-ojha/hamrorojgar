from rest_framework import serializers
from api.models import JobApplication


class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = ['cv', 'vacancy', 'citizen']
