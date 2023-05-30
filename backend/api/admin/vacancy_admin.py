from django.contrib import admin
from api.models import Vacancy, Qualification
from django.forms.models import BaseInlineFormSet
from django.utils.safestring import mark_safe
from itertools import islice
from utils.get_table_field_button import get_table_field_button


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
