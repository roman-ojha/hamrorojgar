from django.urls import path
from api.views import Citizen, Registration, Login, VacancyView, ApplyView
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('citizens/register', Registration.as_view(), name='citizen-register'),
    path('citizens/login', Login.as_view(), name='citizen-login'),
    path('jobs', VacancyView.as_view(), name='job-vacancies'),
    path('job-application', ApplyView.as_view(), name='job-apply'),
    path('gettoken', obtain_auth_token),
]
