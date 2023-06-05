from django.contrib import admin
from .models import Citizen


@admin.register(Citizen)
class CitizenAdmin(admin.ModelAdmin):
    list_display = ['name', 'mobile',
                    'date_of_birth', 'gender', 'citizenship_no']
