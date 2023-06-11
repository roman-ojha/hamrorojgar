from django.db import models
from api.models import district


class TypeChoices(models.TextChoices):
    MAHANAGAR = "MAHAHAGAR", "Mahanagar Palika"
    UPAMAHANAGAR = "UPAMAHANAGAR", "Upamahanagar Palika"
    NAGARPALIKA = "NAGARPALIKA", "Nagar Palika"
    GHAUPALIKA = "GHAUPALIKA", "Ghau Palika"


class Municipality(models.Model):
    name = models.CharField(max_length=35)
    type = models.CharField(max_length=20, choices=TypeChoices.choices)
    district = models.ForeignKey(
        district.District, on_delete=models.CASCADE, related_name='of_district')
