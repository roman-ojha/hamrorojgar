from rest_framework import serializers
from api.models import vacancy
from .government_serializer import GovernmentSerializer
from .qualification_serializer import QualificationSerializer


class VacancySerializer(serializers.ModelSerializer):
    government = GovernmentSerializer()
    qualifications = QualificationSerializer(many=True)

    class Meta:
        model = vacancy.Vacancy
        fields = ['id', 'title', 'description', 'is_opened', 'salary_from',
                  'salary_to', 'opened_at', 'job_type', 'government', 'qualifications', 'job_location_desc']
