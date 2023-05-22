from django.db import models
from . import CitizenUser, Vacancy
import os
from rest_framework.settings import settings


class JobApplication(models.Model):
    cv = models.ImageField(upload_to=os.path.join(
        settings.BASE_DIR, "static", "upload", "job_application"))
    is_approved = models.BooleanField(default=False)
    citizen = models.ForeignKey(
        CitizenUser, on_delete=models.CASCADE, related_name='applied_by')
    vacancy = models.ForeignKey(
        Vacancy, on_delete=models.CASCADE, related_name='applied_vacancy')
