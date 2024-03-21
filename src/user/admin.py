from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from user.models import User


@admin.register(User)
class UserAdmin(UserAdmin, admin.ModelAdmin):
    list_display = (
        "email",
        "firstname",
        "middlename",
        "lastname",
        "is_active",
        "is_verified",
        "is_superuser",
        "is_deleted",
        "created_at",
    )
    list_display_links = ("email",)
    list_filter = (
        "is_active",
        "is_verified",
        "is_deleted",
        "is_superuser",
        "created_at",
    )
    readonly_fields = ("created_at", "last_login")
    search_fields = ("email",)
    ordering = ("-created_at",)
    list_per_page = 15
    fieldsets = (
        (
            "General",
            {
                "fields": (
                    "email",
                    "password",
                    "firstname",
                    "lastname",
                    "middlename",
                    "groups",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_admin",
                    "is_verified",
                    "is_superuser",
                    "is_active",
                    "is_deleted",
                    "is_staff",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                ),
            },
        ),
    )
