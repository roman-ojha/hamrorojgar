from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.db.models.query import QuerySet
from django.utils.translation import gettext_lazy as _
from . import User


class CitizenUserManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.CITIZEN)


class CitizenUser(User):
    base_role = User.Role.CITIZEN

    class Meta:
        proxy = True
        verbose_name = "Citizen"  # Human readable name for admin site

    citizenuser = CitizenUserManager()


class Citizen(models.Model):
    user = models.OneToOneField(
        CitizenUser, on_delete=models.CASCADE, related_name='citizen')
    # _("<human_readable_name>")
    f_name = models.CharField(_("First name"), max_length=30)
    m_name = models.CharField(_("Middle name"), max_length=30, null=True)
    l_name = models.CharField(_("Last name"), max_length=30)
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
