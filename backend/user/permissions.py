from rest_framework import permissions
from rest_framework.exceptions import ValidationError


class IsCustomer(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.role == 1:
            return True
        return ValidationError("Not Customer")


class IsSupplier(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.role == 2:
            return True
        raise ValidationError("Not Supplier")
