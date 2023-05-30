from django.urls import path
from api.views import CitizenView, Registration, Login, JobListView, ApplyView, CitizenLogout


urlpatterns = [
    path('citizen/register', Registration.as_view(), name='citizen-register'),
    path('citizen/login', Login.as_view(), name='citizen-login'),
    path('citizen', CitizenView.as_view(), name='citizen'),
    path('citizen/logout', CitizenLogout.as_view(), name='citizen-logout'),
    path('job', JobListView.as_view(), name='jobs'),
    path('job/apply', ApplyView.as_view(), name='job-apply'),
]
