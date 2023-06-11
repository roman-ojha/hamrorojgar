from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register
from api.models import vacancy


@register(vacancy.Vacancy)
class VacancyIndex(AlgoliaIndex):
    fields = ('title', 'description', 'get_job_type', 'job_location_desc')
    should_index = 'is_closed'
    tags = "get_tag_list"
