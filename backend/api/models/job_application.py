from django.db import models
from api.models import citizen, vacancy
import os
from rest_framework.settings import settings


class JobApplication(models.Model):
    cv = models.ImageField(upload_to=os.path.join(
        settings.BASE_DIR, "static", "upload", "job_application"))
    description = models.TextField(null=True)
    is_approved = models.BooleanField(default=False)
    citizen = models.ForeignKey(
        citizen.CitizenUser, on_delete=models.CASCADE, related_name='applied_by')
    vacancy = models.ForeignKey(
        vacancy.Vacancy, on_delete=models.CASCADE, related_name='applied_vacancy')
    # payment_status = status = models.CharField(
    #     max_length=10, choices=payment.Payment.StatusChoices.choices)
