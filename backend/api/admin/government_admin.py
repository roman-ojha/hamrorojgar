from django.contrib import admin
from api.models import User, GovernmentUser, Government
from django.forms.models import BaseInlineFormSet
from django import forms


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
