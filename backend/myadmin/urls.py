from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('api/jobapplication/<int:id>/view/',
         views.view_job_application, name="view_job_application"),
    path('', admin.site.urls),
]
