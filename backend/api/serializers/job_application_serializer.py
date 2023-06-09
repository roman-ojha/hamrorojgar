from rest_framework import serializers
from api.models import job_application


class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = job_application.JobApplication
        fields = ['cv', 'vacancy', 'citizen', 'description', 'payment_status']
