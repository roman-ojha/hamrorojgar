from typing import Optional, Type
from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from api.models import User, CitizenUser, Citizen, GovernmentUser, Government
from django.forms.models import BaseInlineFormSet
from django import forms


@admin.register(CitizenUser)
class CitizenUserAdmin(admin.ModelAdmin):
    # To show the 'Citizen' data & Insert new data for Citizen on the same 'CitizenUser' Model Admin
    class Inline(admin.StackedInline):
        class InlineFormSet(BaseInlineFormSet):
            model = Citizen
        model = Citizen
        can_delete = False
        formset = InlineFormSet

    def first_name(self, obj):
        return obj.citizen.f_name

    def middle_name(self, obj):
        return obj.citizen.m_name

    def last_name(self, obj):
        return obj.citizen.l_name

    def mobile(self, obj):
        return obj.citizen.mobile

    def date_of_birth(self, obj):
        return obj.citizen.date_of_birth

    def gender(self, obj):
        return obj.citizen.gender

    def nationality(self, obj):
        return obj.citizen.nationality

    def citizenship_no(self, obj):
        return obj.citizen.citizenship_no

    def photo_url(self, obj):
        return obj.citizen.photo_url
    first_name.short_description = "First Name"
    middle_name.short_description = "Middle Name"
    last_name.short_description = "Last Name"
    mobile.short_description = "Mobile No."
    date_of_birth.short_description = "DOB"
    gender.short_description = "Gender"
    nationality.short_description = "Nationality"
    citizenship_no.short_description = "CitizenShip No."
    photo_url.short_description = "Photo URL"

    list_display = ('id', 'email', 'first_name', 'middle_name', 'last_name', 'mobile',
                    'date_of_birth', 'gender', 'nationality', 'citizenship_no', 'photo_url', 'last_login', 'is_superuser', 'is_staff', 'is_active')
    inlines = [Inline]

    class Form(forms.ModelForm):
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)
            # selecting 'Citizen' by default on 'role' select option field
            self.fields['role'].initial = User.Role.CITIZEN
    form = Form


@admin.register(GovernmentUser)
class GovernmentUserAdmin(admin.ModelAdmin):
    class Inline(admin.StackedInline):
        class InlineFormSet(BaseInlineFormSet):
            model = Government
        model = Government
        can_delete = False
        formset = InlineFormSet

    def gov_type(self, obj):
        return obj.government.gov_type
    gov_type.short_description = "Government Type"
    list_display = ('id', 'email', 'gov_type', 'last_login',
                    'is_superuser', 'is_staff', 'is_active')
    inlines = [Inline]

    class Form(forms.ModelForm):
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)
            self.fields['role'].initial = User.Role.GOVERNMENT
    form = Form


# @admin.register(Government)
# class GovernmentUserAdmin(admin.ModelAdmin):
#     list_display = ('id', 'gov_type')
