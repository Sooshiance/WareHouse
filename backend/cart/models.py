from django.db import models

from shortuuid.django_fields import ShortUUIDField

from warehouse.models import Warehouse, Product
from customer.models import Customer


class Order(models.Model):
    warehouse   = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='warehouses')
    customer    = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customers')
    description = models.CharField(max_length = 255)
    order_date  = models.DateTimeField(auto_now_add=True)
    sku         = ShortUUIDField(max_length=40, db_index=True, unique=True, alphabet="0123456789abcdefghij")

    def __str__(self):
        return f"Order {self.sku} by {self.customer.user.username}"


class OrderItem(models.Model):
    order    = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product  = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    sku      = ShortUUIDField(max_length=40, db_index=True, unique=True, alphabet="0123456789abcdefghij")
    
    def get_total_price(self):
        return self.quantity * self.product.price
    
    def __str__(self):
        return f"{self.order.customer.user.username}"
    
    class Meta:
        verbose_name = 'Order Item'
        verbose_name_plural = 'Order Items'
