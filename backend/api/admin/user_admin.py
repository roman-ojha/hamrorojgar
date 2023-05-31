from typing import Any
from api.models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin


@admin.register(User)
class UsersAdmin(UserAdmin):
    list_display = ('id', 'email',)
    ordering = ('email',)
    exclude = ('username', )
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

    # def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
    #     if not change:
    #         obj = User.objects.create_user(
    #             email=form.cleaned_data['email'],
    #             password=form.cleaned_data['password1'],
    #             role=form.cleaned_data['role'],
    #         )
    #         self.log_addition(request, obj)
    #         return obj
    #     # Handle updating existing user record
    #     obj.email = form.cleaned_data['email']
    #     obj.role = form.cleaned_data['role']
    #     # print(form.cleaned_data)
    #     obj.set_password(form.cleaned_data['password'])
    #     obj.save()
    #     self.log_change(request, obj, form.changed_data)
    #     return obj
