from rest_framework import serializers

from .models import Customer

from user.serializers import UserSerializer


class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Customer
        exclude = ["role"]
