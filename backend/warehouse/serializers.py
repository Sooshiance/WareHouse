from rest_framework import serializers

from .models import (Warehouse,
                     Category,
                     Product)

from supplier.serializers import SupplierSerializer


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    supplier = SupplierSerializer()
    category = CategorySerializer()

    class Meta:
        model = Product
        exclude = ['sku', 'is_active']
