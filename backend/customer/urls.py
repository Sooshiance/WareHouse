from django.urls import path

from .views import CustomerGenericAPIView


app_name = "customer"

urlpatterns = [
    path("detail/", CustomerGenericAPIView.as_view(), name='detail'),
]
