from django.db import models
from api.models import vacancy


class Qualification(models.Model):
    description = models.TextField()
    vacancy = models.ForeignKey(
        vacancy.Vacancy, on_delete=models.CASCADE, related_name='qualifications')
