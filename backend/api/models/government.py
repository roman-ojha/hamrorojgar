from typing import Any
from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.db.models.query import QuerySet
from . import User


class GovernmentUserManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs) -> QuerySet:
        result = super().get_queryset(*args, **kwargs)
        return result.filter(role=User.Role.GOVERNMENT)


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
