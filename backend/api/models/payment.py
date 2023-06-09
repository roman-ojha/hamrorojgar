from django.db import models
from api.models import payment_gateway, user


class Payment(models.Model):
    amount = models.IntegerField()  # in cent
    payment_using = models.ForeignKey(
        payment_gateway.PaymentGateway, on_delete=models.CASCADE)
    from_acc = models.CharField(max_length=100, null=True)
    # to_acc

    class StatusChoices(models.TextChoices):
        COMPLETED = "COMPLETED", "Completed"
        PENDING = "PENDING", "Pending"
        REFUSED = "REFUSED", "Refused"
        EXPIRED = "EXPIRED", "Expired"

    status = models.CharField(max_length=10, choices=StatusChoices.choices)
    # id that payment gateway give us before transaction happen
    payment_id = models.CharField(max_length=100, null=True)
    transaction_id = models.CharField(max_length=100, null=True)
    by = models.ForeignKey(user.User, on_delete=models.CASCADE)
    from api.models import job_application
    for_application = models.ForeignKey(
        job_application.JobApplication, on_delete=models.CASCADE)
    # user_mobile for khalti payment
