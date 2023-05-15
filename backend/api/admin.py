from django.contrib import admin
from api.models import User, CitizenUser, Citizen


# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('id', 'email')


@admin.register(CitizenUser)
class CitizenUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')


@admin.register(Citizen)
class CitizenAdmin(admin.ModelAdmin):
    list_display = ('id', 'f_name')
