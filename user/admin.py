from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


class AdminSite(UserAdmin):


    fieldsets = (
    (None, {"fields": ("username", "password")}),
    (("Personal info"), {"fields": ("first_name", "last_name", "email")}),
    (
    ("Permissions"),
    {
    "fields": (
    "is_active",
    "is_staff",
    "is_superuser",
    ),
    },
    ),

    )

admin.site.unregister(User)
admin.site.register(User, AdminSite)