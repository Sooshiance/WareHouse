from django.contrib import admin

from .models import Supplier


class SupplierAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_approved', 'sid')
    list_filter = ['is_approved']


admin.site.register(Supplier, SupplierAdmin)
