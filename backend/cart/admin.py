from django.contrib import admin

from .models import (Order,
                     OrderItem,)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer',)


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order']


admin.site.register(Order, OrderAdmin)

admin.site.register(OrderItem, OrderItemAdmin)
