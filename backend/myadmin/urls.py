from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
    path('api/jobapplication/<int:id>/view/',
         views.view_job_application, name="view_job_application"),
    path('api/jobapplication/<int:id>/approve',
         views.approve_job_application, name="job_application_approve"),
    path('api/jobapplication/<int:id>/disapprove',
         views.disapprove_job_application, name='job_application_disapprove'),
    path('', views.index),
    path('', include('admin_argon.urls')),
    path('', admin.site.urls),
]
