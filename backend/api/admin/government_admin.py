from django.contrib import admin
from api.models import User, GovernmentUser, Government
from django.forms.models import BaseInlineFormSet
from django import forms
from django.contrib.auth.admin import UserAdmin


@admin.register(GovernmentUser)
class GovernmentUserAdmin(UserAdmin):
    class Inline(admin.StackedInline):
        class InlineFormSet(BaseInlineFormSet):
            model = Government
        model = Government
        can_delete = False
        # formset = InlineFormSet
        fieldsets = (
            (None, {
                "fields": ("gov_type", "location",),
            }),
        )

    def gov_type(self, obj):
        return obj.government.get_gov_type_display()
    gov_type.short_description = "Government Type"

    list_display = ('id', 'email', 'gov_type', 'last_login',
                    'is_superuser', 'is_staff', 'is_active')
    inlines = [Inline]
    ordering = ('email',)
    exclude = ('username',)
    add_fieldsets = (
        ("User:", {
            "fields": ("email", "password1", "password2"),
        }),
        ('Permissions:', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
    )

    fieldsets = (
        ("User:", {
            "fields": ("email", "password", "role"),
        }),
        ('Permissions:', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important Dates:', {
            'fields': ('last_login', 'date_joined'),
        }),
    )
