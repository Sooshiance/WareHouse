from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User, Profile


class UserAdmin(BaseUserAdmin):
    list_display = ["phone", "email", "username"]
    filter_horizontal = ()
    list_filter = ("is_superuser", "role")
    fieldsets = ()
    search_fields = ["email"]


class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user",)
    list_filter = ["role"]


admin.site.register(User, UserAdmin)


admin.site.register(Profile, ProfileAdmin)
