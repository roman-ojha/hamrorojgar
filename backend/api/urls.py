from django.urls import path
from api.views import Citizen, Registration, Login

urlpatterns = [
    path('citizens/register', Registration.as_view(), name='citizen-register'),
    path('citizens/login', Login.as_view(), name='citizen-login'),
]
