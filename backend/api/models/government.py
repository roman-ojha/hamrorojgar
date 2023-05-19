from typing import Any
from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.db.models.query import QuerySet
from . import User


class GovernmentUserManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs) -> QuerySet:
        result = super().get_queryset(*args, **kwargs)
        return result.filter(role=User.Role.GOVERNMENT)

    # overriding the 'create_user' method to so that password will get properly hashed
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_active", True)

        if not email:
            raise ValueError("The Email field must be set")

        email = self.normalize_email(email=email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user


class GovernmentUser(User):
    base_role = User.Role.GOVERNMENT

    class Meta:
        proxy = True
        verbose_name = "Government"  # Human readable name for admin site

    user = GovernmentUserManager()


class Government(models.Model):
    user = models.OneToOneField(
        GovernmentUser, on_delete=models.CASCADE, related_name='government')

    class GovernmentType(models.TextChoices):
        FEDERAL = 'F', "Federal"
        PROVINCE = 'P', "Province"
        LOCAL = 'L', "Local"
    gov_type = models.CharField(max_length=3, choices=GovernmentType.choices)
    # location

    def __str__(self) -> str:
        return self.user.email
