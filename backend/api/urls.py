from django.urls import path
from api.views import Citizen, Registration, Login, VacancyView, ApplyView


urlpatterns = [
    path('citizen/register', Registration.as_view(), name='citizen-register'),
    path('citizen/login', Login.as_view(), name='citizen-login'),
    path('jobs', VacancyView.as_view(), name='job-vacancies'),
    path('job-application', ApplyView.as_view(), name='job-apply'),
]
