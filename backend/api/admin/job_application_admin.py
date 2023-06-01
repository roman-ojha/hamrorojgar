from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from api.models import JobApplication, Vacancy
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from admin_numeric_filter.admin import SingleNumericFilter
from utils.get_table_field_button import get_table_field_button


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

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        vacancies = Vacancy.objects.filter(pk=request.user.pk).values('pk')
        return qs.filter(vacancy__in=vacancies)
