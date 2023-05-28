from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import UserAccount, UserProfile


class Admin(UserAdmin):
    list_display = ("email", "username")
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    search_fields = ("email", "username", "phone")


class Profile(admin.ModelAdmin):
    list_display = ("user", "email", "created_at")
    search_fields = ("user", "email", "username")


admin.site.register(UserAccount, Admin)

admin.site.register(UserProfile, Profile)
