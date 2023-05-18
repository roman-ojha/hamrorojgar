from django.contrib import admin
from api.models import User, CitizenUser, Citizen, GovernmentUser, Government, Vacancy, Qualification, JobApplication
from django.forms.models import BaseInlineFormSet
from django import forms
from django.utils.safestring import mark_safe
from itertools import islice


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


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    def salary(self, obj):
        return f"{obj.salary_from}K - {obj.salary_to}K"

    def desc(self, obj):
        if (len(obj.description) > 40):
            return f"{obj.description[0:40]}..."
        else:
            return obj.description
    desc.short_description = "Description"

    def qualifications(self, obj):
        descriptions = [
            "-> " + q.description for q in islice(obj.of_vacancy.all(), 3)]
        return mark_safe('<br>'.join(descriptions))

    def opened_by(self, obj):
        return mark_safe(f'<a href="/admin/api/governmentuser/{obj.government.pk}/change">{obj.government}</a>')

    list_display = ('id', 'title', 'desc', 'salary',
                    'is_opened', 'opened_on', 'job_type', 'opened_by', 'qualifications')

    class Inline(admin.StackedInline):
        class InlineFormSet(BaseInlineFormSet):
            model = Qualification
        model = Qualification
        can_delete = False
        formset = InlineFormSet
    inlines = [Inline]


@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('cv_url', 'is_approved', 'citizen')
