from django.urls import path
from api.views.auth_view import CitizenRegister, CitizenLogin, CitizenLogout
from api.views.citizen_view import CitizenView
from api.views.job_application import ApplyView
from api.views.vacancy_view import JobListView


urlpatterns = [
    path('citizen/register', CitizenRegister.as_view(), name='citizen-register'),
    path('citizen/login', CitizenLogin.as_view(), name='citizen-login'),
    path('citizen/logout', CitizenLogout.as_view(), name='citizen-logout'),
    path('citizen', CitizenView.as_view(), name='citizen'),
    path('job', JobListView.as_view(), name='jobs'),
    path('job/apply', ApplyView.as_view(), name='job-apply'),
]
