from rest_framework import serializers

from .models import (Order,
                     OrderItem,)


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['description']


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['quantity']
