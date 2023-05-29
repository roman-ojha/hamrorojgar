from typing import Any, Dict, List, Optional, Tuple
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from api.models import User, CitizenUser, Citizen, GovernmentUser, Government, Vacancy, Qualification, JobApplication
from django.forms.models import BaseInlineFormSet
from django import forms
from django.utils.safestring import mark_safe
from itertools import islice
from django.utils.html import format_html
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from admin_numeric_filter.admin import SingleNumericFilter
from django.db.models import Q
from utils.get_table_field_button import get_table_field_button


@admin.register(CitizenUser)
class CitizenUserAdmin(UserAdmin):
    def first_name(self, obj):
        return obj.citizen.f_name
    first_name.short_description = "First Name"

    def middle_name(self, obj):
        return obj.citizen.m_name
    middle_name.short_description = "Middle Name"

    def last_name(self, obj):
        return obj.citizen.l_name
    last_name.short_description = "Last Name"

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
        return mark_safe(f'<img width="30px" height="30px" src="/{obj.citizen.photo}"></img>')
    photo.short_description = "Profile Picture"

    def p_address(self, obj):
        return obj.citizen.p_address
    p_address.short_description = "Permanent Address"
    list_display = ('id', 'photo', 'email', 'first_name', 'middle_name', 'last_name', 'mobile',
                    'date_of_birth', 'gender', 'nationality', 'p_address', 'citizenship_no', 'last_login', 'is_superuser', 'is_staff', 'is_active')

    # To show the 'Citizen' data & Insert new data for Citizen on the same 'CitizenUser' Model Admin
    class CitizenInline(admin.StackedInline):
        class CitizenInlineFormSet(BaseInlineFormSet):
            model = Citizen
        model = Citizen
        can_delete = False
        # formset = CitizenInlineFormSet
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


@admin.register(GovernmentUser)
class GovernmentUserAdmin(admin.ModelAdmin):
    class Inline(admin.StackedInline):
        class InlineFormSet(BaseInlineFormSet):
            model = Government
        model = Government
        can_delete = False
        formset = InlineFormSet

    def gov_type(self, obj):
        return obj.government.get_gov_type_display()
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
            "* " + q.description[0:30] + " ..."if len(q.description) > 30 else "* " + q.description for q in islice(obj.qualifications.all(), 3)]
        return mark_safe('<br>'.join(descriptions))

    def opened_by(self, obj):
        return mark_safe(f'<a href="/admin/api/governmentuser/{obj.government.pk}/change">{obj.government}</a>')

    def job_applications(self, obj):
        return mark_safe(f'{get_table_field_button(f"/admin/api/jobapplication/?vacancy_id={obj.id}")}')

    list_display = ('id', 'title', 'desc', 'job_applications', 'salary',
                    'is_opened', 'opened_at', 'job_type', 'opened_by', 'qualifications')
    ordering = ('id',)

    class Inline(admin.StackedInline):
        class InlineFormSet(BaseInlineFormSet):
            model = Qualification
        model = Qualification
        can_delete = False
        formset = InlineFormSet
    inlines = [Inline]


@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        self.filtered_vacancy_id = request.GET.get('vacancy_id')
        return super().get_queryset(request)

    def of_vacancy(self, obj):
        return mark_safe(f'<a href="/admin/api/vacancy/{obj.vacancy}/change">{obj.vacancy}</a>')

    def applied_by(self, obj):
        return mark_safe(f'<a href="/admin/api/citizenuser/{obj.citizen.id}/change">{obj.citizen}</a>')

    def cv_image(self, obj):
        return format_html(f'<img src="/{obj.cv}" />', obj.cv)
    cv_image.short_description = 'CV Image'

    def detail(self, obj):
        return mark_safe(f'{get_table_field_button(f"/admin/api/jobapplication/{obj.id}/view/")}')

    def cv_url(self, obj):
        return obj.cv

    def change_view(self, request: HttpRequest, object_id: str, form_url='', extra_context=None):
        # Add the cv_image to the extra_context
        extra_context = extra_context or {}
        job_application = self.get_object(request, object_id)
        extra_context['cv_image'] = self.cv_image(job_application)
        extra_context['cv_url'] = self.cv_url(job_application)
        return super().change_view(request, object_id, form_url, extra_context=extra_context)
    list_display = ('id', 'detail', 'applied_by', 'is_approved', 'of_vacancy')
    ordering = ('id',)

    fields = ('cv', 'citizen', 'vacancy', 'description',)

    class VacancyFilter(SingleNumericFilter):
        title = "Vacancy"
        parameter_name = 'vacancy_id'

        def queryset(self, request, queryset):
            if not self.value():
                return queryset
            if self.value():
                # Assuming 'self.value()' contains the ID of the desired vacancy
                vacancy_id = int(self.value())
                return queryset.filter(vacancy_id=vacancy_id)

    list_filter = (('vacancy__id', VacancyFilter),)
