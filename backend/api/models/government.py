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

    government = GovernmentUserManager()
