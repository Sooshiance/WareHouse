from rest_framework import generics, permissions

from .models import (Order,
                     OrderItem,)
from .serializers import (OrderSerializer,
                          OrderItemSerializer,)

from user.permissions import IsCustomer


class OrderCreateGenericAPIView(generics.ListCreateAPIView):
    permission_classes = [IsCustomer]
    serializer_class = OrderSerializer

    def get_object(self):
        return 
