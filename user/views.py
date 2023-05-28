from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordResetView, PasswordResetConfirmView, PasswordResetCompleteView
)

from .models import UserAccount
from .forms import RegisterForm


class LoginPageView(LoginView):
    template_name = "login.html"
    
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return reverse_lazy("/")
        return super().get(request, *args, **kwargs)


class LogoutPageView(LogoutView):
    template_name = "logout.html"


class SignupPageView(FormView):
    template_name = "register.html"
    form_class = RegisterForm
    success_url = reverse_lazy("/")
    
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return reverse_lazy("/")
        return super().get(request, *args, **kwargs)
    
    def form_valid(self, form):
        new_user = UserAccount.objects.create_user(
            email=form.cleaned_data['email'],
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password'],
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
            pic=form.cleaned_data['pic'],
            description=form.cleaned_data['description'],
            
            # TODO : If you add other fields to your model, include them here
        )
        return super().form_valid(form)


class PasswordChangePageView(PasswordResetView):
    template_name ="pass_change.html"
    email_template_name = "pass_change_email.html"
    subject_template_name = "password_reset_subject.txt"
    success_message ="""  We've emailed you instructions for setting your password,
                      if an account exists with the email you entered. You should receive them shortly.
                      If you don't receive an email,
                      please make sure you've entered the address you registered with, and check your spam folder. """
    success_url = reverse_lazy("/")


class PasswordResetConfirmViewPage(PasswordResetConfirmView):
    template_name = "password_reset_confirm.html"


class PasswordResetCompleteViewPage(PasswordResetCompleteView):
    template_name = "password_reset_complete.html"
