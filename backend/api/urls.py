from django.urls import path
from api.views import Citizen, Registration, Login, VacancyView

urlpatterns = [
    path('citizens/register', Registration.as_view(), name='citizen-register'),
    path('citizens/login', Login.as_view(), name='citizen-login'),
    path('vacancy/', VacancyView.as_view(), name="vacancy")
]
