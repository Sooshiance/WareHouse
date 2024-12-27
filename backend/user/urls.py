from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView

from .views import (
    CustomTokenObtainPairView,
    RegisterUserGenericAPIView,
    ProfileGenericAPIView,
)


app_name = "user"

urlpatterns = [
    path("access/token/", CustomTokenObtainPairView.as_view()),
    path("refresh/token/", TokenRefreshView.as_view()),
    path("register/user/", RegisterUserGenericAPIView.as_view()),
    path("profile/user/", ProfileGenericAPIView.as_view()),
]
