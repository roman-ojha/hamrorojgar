from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register
from api.models import vacancy


@register(vacancy.Vacancy)
class VacancyIndex(AlgoliaIndex):
    fields = ('id', 'title', 'description', 'job_type')
    should_index = 'is_closed'
    tags = "get_tag_list"
