from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User
from .forms import UserCreateForm, UserUpdateForm

class CustomUserAdmin(UserAdmin):
    add_form = UserCreateForm
    form = UserUpdateForm
    empty_value_display='-------'

    readonly_fields = ['created_date', 'updated_date', 'password']

    list_display = (
        "first_name",
        "last_name",
        "cpf",
        "email",
        "is_active",
        "is_superuser",
        "created_date",
        "updated_date",
    )

    list_filter = (
        "first_name",
        "last_name",
        "cpf",
        "email",
        "last_login",
        "is_active",
        "is_superuser",
        "created_date",
        "updated_date",
    )

    fieldsets = (
        (
            "Informações básicas",
            {
                "classes": ("grp-collapse grp-open",),
                "fields": (("first_name", "last_name"), "email", "password"),
            },
        ),
        (
            "Permissões",
            {"classes": ("grp-collapse grp-open",), "fields": ("is_superuser","is_staff")},
        ),
        ("Status", {"classes": ("grp-collapse grp-open",), "fields": ("is_active",)}),
    )

    add_fieldsets = (
        (
            "Login",
            {
                "classes": ("grp-collapse grp-open", "wide"),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )

    search_fields = (
        "first_name",
        "last_name",
        "email",
        "last_login",
        "is_active",
        "is_superuser",
        "created_date",
        "updated_date",
    )

    ordering = ("first_name", "created_date")
    filter_horizontal = ()


admin.site.register(User,CustomUserAdmin)

# Register your models here.
