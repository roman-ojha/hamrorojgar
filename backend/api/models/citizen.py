from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.db.models.query import QuerySet
from django.utils.translation import gettext_lazy as _
from . import User


class CitizenUserManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.CITIZEN)

    # overriding the 'create_user' method to so that password will get properly hashed

    def create_user(self, email, password=None, **extra_fields):
        print("hello =========================")
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_active", True)

        if not email:
            raise ValueError("The Email field must be set")

        email = self.normalize_email(email=email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        # user.save()
        print(user.password)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        return self.create_user(email=email, password=password, **extra_fields)


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

    class GenderChoice(models.TextChoices):
        MALE = 'M', 'Male'
        FEMALE = 'F', 'Female'
        OTHERS = 'O', 'Others'
    gender = models.CharField(
        max_length=3, choices=GenderChoice.choices)
    nationality = models.CharField(max_length=80)
    citizenship_no = models.CharField(max_length=200)
    # Use url shortener package for photo url link
    photo_url = models.TextField(max_length=100, null=True)
    # permanent_address
    # temporary_address
