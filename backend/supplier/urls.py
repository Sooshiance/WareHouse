from django.urls import path

from .views import SupplierGenericAPIVIew


app_name = "supplier"

urlpatterns = [
    path("verify/", SupplierGenericAPIVIew.as_view()),
]
