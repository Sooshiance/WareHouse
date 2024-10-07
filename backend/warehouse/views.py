from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError

from .models import (Warehouse,
                     Category,
                     Product)
from .serializers import (WarehouseSerializer,
                          CategorySerializer,
                          ProductSerializer,)


class WareHouseGenericAPIView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = WarehouseSerializer
    queryset = Warehouse.objects.all()


class WareHouseDetailGenericAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = WarehouseSerializer

    def get_object(self):
        sku = self.kwargs['sku']
        return sku
    
    def get_queryset(self):
        sku = self.get_object()
        try:
            return Warehouse.objects.get(sku=sku)
        except Exception as e:
            raise ValidationError("No WareHouse found!")


class CategoryGenericAPIView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryDetailGenericAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = CategorySerializer

    def get_object(self):
        sku = self.kwargs['sku']
        return sku
    
    def get_queryset(self):
        sku = self.get_object()
        try:
            return Category.objects.get(sku=sku)
        except Exception as e:
            raise ValidationError("No Category found!")


class ProductGenericAPIView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductDetailGenericAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = ProductSerializer

    def get_object(self):
        sku = self.kwargs['sku']
        return sku
    
    def get_queryset(self):
        sku = self.get_object()
        try:
            return Product.objects.get(sku=sku)
        except Exception as e:
            raise ValidationError("No Product found!")
