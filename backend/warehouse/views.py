from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError, NotFound

from .models import Warehouse, Category, Product
from .serializers import (
    WarehouseSerializer,
    CategorySerializer,
    ProductSerializer,
)

from supplier.permissions import CanSupply


class WareHouseGenericAPIView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = WarehouseSerializer
    queryset = Warehouse.objects.all()


class WareHouseDetailGenericAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = WarehouseSerializer

    def get_object(self):
        sku = self.kwargs["sku"]
        return sku

    def get_queryset(self):
        sku = self.get_object()
        try:
            return Warehouse.objects.get(sku=sku)
        except NotFound as e:
            raise ValidationError(str(e))


class CategoryGenericAPIView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryDetailGenericAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = CategorySerializer

    def get_object(self):
        sku = self.kwargs["sku"]
        return sku

    def get_queryset(self):
        sku = self.get_object()
        try:
            return Category.objects.get(sku=sku)
        except NotFound as e:
            raise ValidationError(str(e))


class ProductGenericAPIView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductDetailGenericAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = ProductSerializer

    def get_object(self):
        sku = self.kwargs["sku"]
        return sku

    def get_queryset(self):
        sku = self.get_object()
        try:
            return Product.objects.get(sku=sku)
        except NotFound as e:
            raise ValidationError(str(e))


class SupplierProductGenericAPIView(generics.ListAPIView):
    permission_classes = [CanSupply]
    serializer_class = ProductSerializer

    def get_queryset(self):
        p = Product.objects.filter(can_supply=True)
        return p
