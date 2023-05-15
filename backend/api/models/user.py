from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email=email)
        user = self.model(
            email=email,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser has to have is_staff being true")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser has to have is_superuser being true")

        return self.create_user(email=email, password=password, **extra_fields)


class User(AbstractUser, PermissionsMixin):
    class Role(models.TextChoices):
        GOVERNMENT = "GOV", "Government"
        CITIZEN = "CITIZEN", "Citizen"

    base_role = Role.GOVERNMENT
    email = models.CharField(max_length=80, unique=True)
    role = models.CharField(
        max_length=15, choices=Role.choices)
    username = None
    first_name = None
    last_name = None
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.email