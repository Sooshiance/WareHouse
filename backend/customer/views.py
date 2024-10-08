from rest_framework import generics

from .models import Customer
from .serializers import CustomerSerializer

from user.permissions import IsCustomer


class CustomerGenericAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsCustomer]
    serializer_class = CustomerSerializer

    def get_queryset(self):
        user = self.request.user
        try:
            c = Customer.objects.get(user=user)
        except Exception as e:
            raise e
        return c
