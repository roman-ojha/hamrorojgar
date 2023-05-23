from django.db import models
from . import Vacancy


class Qualification(models.Model):
    description = models.TextField()
    vacancy = models.ForeignKey(
        Vacancy, on_delete=models.CASCADE, related_name='qualifications')
