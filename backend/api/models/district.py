from django.db import models


class District(models.Model):
    name = models.CharField(max_length=30)
