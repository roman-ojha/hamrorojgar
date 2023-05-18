from django.db import models
from . import CitizenUser, Vacancy


class JobApplication(models.Model):
    cv_url = models.TextField(max_length=100)
    is_approved = models.BooleanField(default=False)
    citizen = models.ForeignKey(
        CitizenUser, on_delete=models.CASCADE, related_name='applied_by')
    vacancy = models.ForeignKey(
        Vacancy, on_delete=models.CASCADE, related_name='applied_vacancy')
