from django.urls import path

from .views import (
    WareHouseGenericAPIView,
    WareHouseDetailGenericAPIView,
    CategoryGenericAPIView,
    CategoryDetailGenericAPIView,
    ProductGenericAPIView,
    ProductDetailGenericAPIView,
)


app_name = "warehouse"

urlpatterns = [
    path("create/warehouse/", WareHouseGenericAPIView.as_view(), name=""),
    path(
        "detail/warehouse/<str:sku>/", WareHouseDetailGenericAPIView.as_view(), name=""
    ),
    path("create/category/", CategoryGenericAPIView.as_view(), name=""),
    path("detail/category/<str:sku>/", CategoryDetailGenericAPIView.as_view(), name=""),
    path("create/product/", ProductGenericAPIView.as_view(), name=""),
    path("detail/product/<str:sku>/", ProductDetailGenericAPIView.as_view(), name=""),
]
