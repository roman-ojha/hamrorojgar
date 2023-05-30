from django.contrib import admin
from api.models import CitizenUser, Citizen
from django.forms.models import BaseInlineFormSet
from django.utils.safestring import mark_safe
from django.contrib.auth.admin import UserAdmin


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
