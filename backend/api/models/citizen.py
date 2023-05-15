from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from . import User


class CitizenUserManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.CITIZEN)


class CitizenUser(User):
    base_role = User.Role.CITIZEN

    class Meta:
        proxy = True

    citizen = CitizenUserManager()


class Citizen(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    f_name = models.CharField(max_length=30)
    m_name = models.CharField(max_length=30, null=True)
    l_name = models.CharField(max_length=30)
    mobile = models.IntegerField()
    date_of_birth = models.DateField()

    class GenderChoice(models.TextChoices):
        MALE = 'M', 'Male'
        FEMALE = 'F', 'Female'
        OTHERS = 'O', 'Others'
    gender = models.CharField(
        max_length=3, choices=GenderChoice.choices)
    nationality = models.CharField(max_length=80)
    citizenship_no = models.CharField(max_length=200)
    # Use url shortener package for photo url link
    photo_url = models.CharField(max_length=100, null=True)
    # permanent_address
    # temporary_address
