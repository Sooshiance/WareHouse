from django.contrib import admin

from .models import Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = ("user",)
    search_fields = ["user__username", "user__email"]


admin.site.register(Customer, CustomerAdmin)
