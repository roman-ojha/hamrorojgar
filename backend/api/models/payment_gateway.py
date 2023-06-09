from django.db import models


class PaymentGateway(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    # image_url
    is_active = models.BooleanField(default=True)
