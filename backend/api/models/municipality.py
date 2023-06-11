from django.db import models
from api.models import district


class TypeChoices(models.TextChoices):
    MAHANAGAR = "MAHAHAGAR", "Mahanagar Palika"
    UPAMAHANAGAR = "UPAMAHANAGAR", "Upamahanagar Palika"
    NAGARPALIKA = "NAGARPALIKA", "Nagar Palika"
    GHAUPALIKA = "GHAUPALIKA", "Ghau Palika"

    def get_type(self, municipality_type) -> str:
        if municipality_type == self.MAHANAGAR:
            return self.MAHANAGAR.label
        elif municipality_type == self.UPAMAHANAGAR:
            return self.UPAMAHANAGAR.label
        elif municipality_type == self.NAGARPALIKA:
            return self.NAGARPALIKA.label
        elif municipality_type == self.GHAUPALIKA:
            return self.GHAUPALIKA.label
        else:
            return ""


class Municipality(models.Model):
    name = models.CharField(max_length=35)
    type = models.CharField(max_length=20, choices=TypeChoices.choices)
    district = models.ForeignKey(
        district.District, on_delete=models.CASCADE, related_name='of_district')

    def get_type_label(self):
        return TypeChoices(self.type).get_type(municipality_type=self.type)
