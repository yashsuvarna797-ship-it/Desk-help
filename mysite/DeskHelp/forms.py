from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=40, required=True)
    class Meta:
        model=User
        fields = ['username', 'password1', 'password2', 'email']

class LoginForm(AuthenticationForm):
    pass
