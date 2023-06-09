from django.db import models
from .payment_gateway import PaymentGateway
from .citizen import Citizen
from .job_application import JobApplication


class Payment(models.Model):
    amount = models.IntegerField()  # in cent
    payment_using = models.OneToOneField(
        PaymentGateway, on_delete=models.CASCADE)
    from_acc = models.CharField(max_length=100, null=True)
    # to_acc

    class StatusChoices(models.TextChoices):
        COMPLETED = "COMPLETED", "Pending"
        PENDING = "PENDING", "Pending"
        REFUSED = "REFUSED", "Refused"
        EXPIRED = "EXPIRED", "Expired"
    status = models.CharField(max_length=10, choices=StatusChoices.choices)
    # id that payment gateway give us before transaction happen
    payment_id = models.CharField(max_length=100, null=True)
    transaction_id = models.CharField(max_length=100, null=True)
    by = models.OneToOneField(Citizen, on_delete=models.CASCADE)
    for_application = models.OneToOneField(
        JobApplication, on_delete=models.CASCADE)
    # user_mobile for khalti payment
