from .citizen_admin import CitizenUserAdmin
from .government_admin import GovernmentUserAdmin
from .job_application_admin import JobApplicationAdmin
from .vacancy_admin import VacancyAdmin

from django.contrib import admin
from django.contrib.auth.models import Group
from rest_framework.authtoken.models import TokenProxy

# admin.site.unregister(Group)
admin.site.unregister(TokenProxy)
