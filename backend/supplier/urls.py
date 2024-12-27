from django.urls import path

from .views import SupplierGenericAPIView


app_name = "supplier"

urlpatterns = [
    path("verify/", SupplierGenericAPIView.as_view()),
]
