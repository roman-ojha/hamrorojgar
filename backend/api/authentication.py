from typing import Any, Optional
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.http.request import HttpRequest
from api.models import User

# Custom 'authentication()' function because I have used 'email' & 'password' as the main auth credential
# UserModel = get_user_model()


# class CustomModelBackend(ModelBackend):
#     def authenticate(self, request, username=None, password=None, **kwargs: Any) -> User | None:
#         # return super().authenticate(request, email, password, **kwargs)
#         try:
#             user = UserModel.objects.get(email=username)
#         except UserModel.DoesNotExist:
#             return None
#         else:
#             if user.check_password(password):
#                 return user
#         return None
