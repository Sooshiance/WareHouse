from django.urls import path

from .views import (
    LoginPageView, LogoutPageView, SignupPageView, PasswordChangePageView, PasswordResetConfirmViewPage,
    PasswordResetCompleteViewPage
)


urlpatterns = [
    path('', LoginPageView.as_view(), name='LOGIN'),
    path('logout/', LogoutPageView.as_view(), name='LOGOUT'),
    path('register/', SignupPageView.as_view(), name='REGISTER'),
    path('change/', PasswordChangePageView.as_view(), name='CHANGE'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmViewPage.as_view(), name='CONFIRM'),
    path('password-reset-complete/', PasswordResetCompleteViewPage.as_view(), name='password_reset_complete'),
]
