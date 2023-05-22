from rest_framework import serializers
from api.models import Vacancy
from .government_serializer import GovernmentSerializer
from .qualification_serializer import QualificationSerializer


class VacancySerializer(serializers.ModelSerializer):
    government = GovernmentSerializer()
    of_vacancy = QualificationSerializer(many=True)

    class Meta:
        model = Vacancy
        fields = ['title', 'description', 'is_opened', 'salary_from',
                  'salary_to', 'opened_at', 'job_type', 'government', 'of_vacancy']
