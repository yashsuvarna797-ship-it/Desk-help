from django.contrib.auth.forms import UserCreationForm, SetPasswordForm, AuthenticationForm, PasswordChangeForm, PasswordResetForm
from . import models
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=40, required=True)
    class Meta:
        model=User
        fields = ['username', 'password1', 'password2', 'email']

class LoginForm(AuthenticationForm):
    pass

class MyPasswordChangeForm(PasswordChangeForm):
    pass

class MyPasswordResetForm(PasswordResetForm):
    pass

class MyResetPasswordForm(SetPasswordForm):
    pass

class TicketForm(forms.ModelForm):
    class Meta:
        model = models.Ticket
        fields = ['title', 'description', 'category']