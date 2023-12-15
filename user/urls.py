from django.urls import path
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetCompleteView

from .views import (LoginPageView, LogoutPageView, SignupPageView)


urlpatterns = [
    path('', LoginPageView.as_view(), name='LOGIN'),
    path('logout/', LogoutPageView.as_view(), name='LOGOUT'),
    path('register/', SignupPageView.as_view(), name='REGISTER'),
    path('change/', PasswordResetView.as_view(template_name ="pass_change.html",
                                                   email_template_name = "pass_change_email.html",
                                                   subject_template_name = "password_reset_subject.txt",
                                                  success_message ="""  We've emailed you instructions for setting your password,
                      if an account exists with the email you entered. You should receive them shortly.
                      If you don't receive an email,
                      please make sure you've entered the address you registered with, and check your spam folder. """,
                                                  success_url = reverse_lazy("/")), name='CHANGE'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name = "password_reset_confirm.html"), name='CONFIRM'),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(template_name = "password_reset_complete.html"), name='password_reset_complete'),
]
