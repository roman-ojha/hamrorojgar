from typing import Optional, Type
from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from api.models import User, CitizenUser, Citizen, GovernmentUser, Government
from django.forms.models import BaseInlineFormSet
from django import forms


# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('id', 'email')


@admin.register(CitizenUser)
class CitizenUserAdmin(admin.ModelAdmin):
    # To show the 'Citizen' data & Insert new data for Citizen on the same 'CitizenUser' Model Admin
    class Inline(admin.StackedInline):
        class InlineFormSet(BaseInlineFormSet):
            model = Citizen
        model = Citizen
        can_delete = False
        formset = InlineFormSet
    list_display = ('id', 'email')
    inlines = [Inline]

    class Form(forms.ModelForm):
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)
            # selecting 'Citizen' by default on 'role' select option field
            self.fields['role'].initial = User.Role.CITIZEN
    form = Form


# @admin.register(Citizen)
# class CitizenAdmin(admin.ModelAdmin):
#     list_display = ('id', 'f_name')


@admin.register(GovernmentUser)
class GovernmentUserAdmin(admin.ModelAdmin):
    class Inline(admin.StackedInline):
        class InlineFormSet(BaseInlineFormSet):
            model = Government
        model = Government
        can_delete = False
        formset = InlineFormSet
    list_display = ('id', 'email')
    inlines = [Inline]

    class Form(forms.ModelForm):
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)
            self.fields['role'].initial = User.Role.GOVERNMENT
    form = Form


# @admin.register(Government)
# class GovernmentUserAdmin(admin.ModelAdmin):
#     list_display = ('id', 'gov_type')
