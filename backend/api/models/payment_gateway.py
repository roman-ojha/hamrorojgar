from django.db import models


class PaymentGateway(models.Model):
    class CodeChoices(models.TextChoices):
        KHALTI = "khalti", "Khalti"
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=50, choices=CodeChoices.choices)
    # image_url
    is_active = models.BooleanField(default=True)
