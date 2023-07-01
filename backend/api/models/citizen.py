from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.db.models.query import QuerySet
from django.utils.translation import gettext_lazy as _
from . import User
from api.models import address
from rest_framework.settings import settings
import os
from utils.generate_unique_hash import generate_unique_hash


class CitizenUserManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.CITIZEN)

    # # overriding the 'create_user' method to so that password will get properly hashed

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_active", True)

        if not email:
            raise ValueError("The Email field must be set")

        email = self.normalize_email(email=email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user


class CitizenUser(User):
    base_role = User.Role.CITIZEN

    class Meta:
        proxy = True
        verbose_name = "Citizen"  # Human readable name for admin site

    objects = CitizenUserManager()


class Citizen(models.Model):
    user = models.OneToOneField(
        CitizenUser, on_delete=models.CASCADE, related_name='citizen')
    # _("<human_readable_name>")
    f_name = models.CharField(_("First name"), max_length=30)
    m_name = models.CharField(_("Middle name"), max_length=30, null=True)
    l_name = models.CharField(_("Last name"), max_length=30)
    mobile = models.IntegerField()
    date_of_birth = models.DateField()
    is_valid_number = models.BooleanField(default=False)
    verification_code = models.TextField(unique=True)
    number_verification_otp = models.IntegerField(default=0)
    d7_otp_id = models.TextField(null=True)

    class GenderChoice(models.TextChoices):
        MALE = 'M', 'Male'
        FEMALE = 'F', 'Female'
        OTHERS = 'O', 'Others'
    gender = models.CharField(
        max_length=3, choices=GenderChoice.choices)
    nationality = models.CharField(max_length=80)
    citizenship_no = models.CharField(max_length=200)
    # Use url shortener package for photo url link
    photo = models.ImageField(upload_to=os.path.join(
        settings.BASE_DIR, "static", "upload", "citizen"))
    p_address = models.OneToOneField(
        address.Address, on_delete=models.CASCADE, related_name='p_address')
    t_address = models.OneToOneField(
        address.Address, on_delete=models.CASCADE, related_name='t_address', null=True)
