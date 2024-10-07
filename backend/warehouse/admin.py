from django.contrib import admin

from .models import (Warehouse,
                     Category,
                     Product)


class WarehouseAdmin(admin.ModelAdmin):
    list_display = ['name']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['is_active']


admin.site.register(Warehouse, WarehouseAdmin)

admin.site.register(Category, CategoryAdmin)

admin.site.register(Product, ProductAdmin)
