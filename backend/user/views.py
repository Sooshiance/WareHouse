from rest_framework import generics, response, status, permissions
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import User, Profile
from .serializers import (
    RegisterSerializer,
    ProfileSerializer,
    CustomTokenObtainPairSerializer,
)


class CustomTokenObtainPairView(TokenObtainPairView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CustomTokenObtainPairSerializer


class RegisterUserGenericAPIView(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer
    queryset = User.objects.all()

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()


class ProfileGenericAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProfileSerializer

    def get(self, request, *args, **kwargs):
        user = request.user
        try:
            profile = Profile.objects.get(user=user)
        except Exception as e:
            raise e
        srz = ProfileSerializer(profile)
        return response.Response(srz.data, status=status.HTTP_200_OK)
