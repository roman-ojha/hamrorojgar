from django.contrib import admin
from api.models import User, CitizenUser, Citizen, GovernmentUser, Government
from django.forms.models import BaseInlineFormSet


# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('id', 'email')


@admin.register(CitizenUser)
class CitizenUserAdmin(admin.ModelAdmin):
    # To show the 'Citizen' data & Insert new data for Citizen on the same 'CitizenUser' Model Admin
    class CitizenInline(admin.StackedInline):
        class CitizenInlineFormSet(BaseInlineFormSet):
            model = Citizen
        model = Citizen
        can_delete = False
        formset = CitizenInlineFormSet
    list_display = ('id', 'email')
    inlines = [CitizenInline]


# @admin.register(Citizen)
# class CitizenAdmin(admin.ModelAdmin):
#     list_display = ('id', 'f_name')


@admin.register(GovernmentUser)
class GovernmentUserAdmin(admin.ModelAdmin):
    class GovernmentInline(admin.StackedInline):
        class GovernmentInlineFormSet(BaseInlineFormSet):
            model = Government
        model = Government
        can_delete = False
        formset = GovernmentInlineFormSet
    list_display = ('id', 'email')
    inlines = [GovernmentInline]


# @admin.register(Government)
# class GovernmentUserAdmin(admin.ModelAdmin):
#     list_display = ('id', 'gov_type')
