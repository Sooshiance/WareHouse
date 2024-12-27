from rest_framework import generics

from .models import Supplier
from .serializers import SupplierSerializer

from user.permissions import IsSupplier


class SupplierGenericAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsSupplier]
    serializer_class = SupplierSerializer

    def get_queryset(self):
        user = self.request.user
        try:
            s = Supplier.objects.get(user=user)
        except Exception as e:
            raise e
        return s
