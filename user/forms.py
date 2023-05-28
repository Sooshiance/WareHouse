from django import forms

from .models import UserAccount


class RegisterForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = [
            'email',
            'username',
            'password',
            'first_name',
            'last_name',
            'pic',
            'description',
            
            # TODO : If you add other fields to your model, include them here
        ]
        labels={
            'email': 'Email', 'username': 'Username', 'password': 'Password',
            'first_name': 'Name', 'last_name': 'Last name', 'pic': 'Profile Picture',
            'description': 'Description',
        }
        
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control my-5'}),
            'username': forms.TextInput(attrs={'class': 'form-control my-5'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control my-5'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control my-5'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control my-5'}),
            'pic': forms.FileInput(attrs={'class': 'form-control my-5'}),
            'description': forms.Textarea(attrs={'class': 'form-control my-5'}),
        }
