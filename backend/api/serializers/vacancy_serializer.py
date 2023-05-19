from rest_framework.serializers import Serializer, ModelSerializer
from api.models import Vacancy


class VacancySerializer(ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ['title', 'description', 'is_opened', 'salary_from',
                  'salary_to', 'opened_on', 'job_type', 'government']
