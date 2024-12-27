from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied


class CanSupply(BasePermission):
    def has_permission(self, request, view):
        if (
            request.user.is_authenticated
            and hasattr(request.user, "user_supplier")
            and request.user.user_supplier.is_approved
        ):
            return True
        raise PermissionDenied(
            detail="The user is not a supplier or Does not has this permission"
        )
