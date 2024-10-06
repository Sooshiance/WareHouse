from rest_framework import serializers

from .models import Supplier

from user.serializers import UserSerializer


class SupplierSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    
    class Meta:
        model = Supplier
        exclude = ['sku', 'is_approved']
