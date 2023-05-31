from typing import Any, Dict, Mapping, Optional, Type, Union
from django.contrib import admin
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from api.models import CitizenUser, Citizen
from django.forms.models import BaseInlineFormSet
from django.utils.safestring import mark_safe
from django.contrib.auth.admin import UserAdmin
from django import forms


# To show the 'Citizen' data & Insert new data for Citizen on the same 'CitizenUser' Model Admin
class CitizenInline(admin.StackedInline):
    class CitizenInlineFormSet(BaseInlineFormSet):
        model = Citizen
    # formset = CitizenInlineFormSet

    class CitizenInlineForm(forms.ModelForm):

        class Meta:
            model = Citizen
            fields = '__all__'

        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)
            self.fields['m_name'].required = False
            self.fields['t_address'].required = False
    model = Citizen
    can_delete = False
    form = CitizenInlineForm
    fieldsets = (
        ("Name:", {
            'fields': (('f_name', 'm_name', 'l_name',),),
        }),
        ("Other Info:", {
            'fields': (('nationality', 'citizenship_no', 'gender', 'date_of_birth', 'mobile'),)
        }),
        ("Permanent Address:", {
            'fields': ('p_address',)
        }),
        ("Temporary Address:", {
            'fields': ('t_address',)
        }),
    )


@admin.register(CitizenUser)
class CitizenUserAdmin(UserAdmin):
    def mobile(self, obj):
        return obj.citizen.mobile
    mobile.short_description = "Mobile No."

    def date_of_birth(self, obj):
        return obj.citizen.date_of_birth
    date_of_birth.short_description = "DOB"

    def gender(self, obj):
        return obj.citizen.get_gender_display()
    gender.short_description = "Gender"

    def nationality(self, obj):
        return obj.citizen.nationality
    nationality.short_description = "Nationality"

    def citizenship_no(self, obj):
        return obj.citizen.citizenship_no
    citizenship_no.short_description = "CitizenShip No."

    def photo(self, obj):
        return mark_safe(f'<img style="border-radius:50%;" width="30px" height="30px" src="/{obj.citizen.photo}"></img>')
    photo.short_description = "Profile Picture"

    def full_name(self, obj):
        if obj.citizen.m_name:
            return f"{obj.citizen.f_name} {obj.citizen.m_name} {obj.citizen.l_name}"
        return f"{obj.citizen.f_name} {obj.citizen.l_name}"

    def p_address(self, obj):
        return obj.citizen.p_address
    p_address.short_description = "Permanent Address"
    list_display = ('id', 'photo', 'email', 'full_name', 'mobile',
                    'date_of_birth', 'gender', 'nationality', 'p_address', 'citizenship_no')

    inlines = [CitizenInline]

    ordering = ('email',)
    exclude = ('username', )  # we are not using 'username' file rather 'email'
    add_fieldsets = (
        ("User", {
            'fields': ('email', 'password1', 'password2',),
        }),
    )
    fieldsets = (
        ("User:", {
            'fields': ('email', 'password', 'role'),
        }),
        ('Permissions:', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important Dates:', {
            'fields': ('last_login', 'date_joined'),
        }),
    )
