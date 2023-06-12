from typing import Any
from django.db import models
from django.db.models import CharField
from api.models import citizen, vacancy
import os
from rest_framework.settings import settings


class JobApplication(models.Model):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        from api.models import payment
        super().__init__(*args, **kwargs)
    cv = models.ImageField(upload_to=os.path.join(
        settings.BASE_DIR, "static", "upload", "job_application"))
    description = models.TextField(null=True)
    is_approved = models.BooleanField(default=False)
    citizen = models.ForeignKey(
        citizen.CitizenUser, on_delete=models.CASCADE, related_name='applied_by')
    vacancy = models.ForeignKey(
        vacancy.Vacancy, on_delete=models.CASCADE, related_name='applied_vacancy')

    class PaymentStatusChoices(models.TextChoices):
        COMPLETED = "COMPLETED", "Completed"
        PENDING = "PENDING", "Pending"
        REFUSED = "REFUSED", "Refused"
        EXPIRED = "EXPIRED", "Expired"
    payment_status = models.CharField(
        max_length=10, choices=PaymentStatusChoices.choices)
    # apply_on
