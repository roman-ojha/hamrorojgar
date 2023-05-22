from django.db import models


class Address(models.Model):
    district = models.CharField(max_length=200)
    municipality = models.CharField(max_length=100)
    ward_no = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.district}, {self.municipality}, {self.ward_no}"
