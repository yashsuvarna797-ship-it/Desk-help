from django.contrib.auth.forms import UserCreationForm, SetPasswordForm, AuthenticationForm, PasswordChangeForm, PasswordResetForm
from . import models
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=40, required=True,
                                label='',
                                widget=forms.TextInput(attrs={
                                    'class':'username-input',
                                    'placeholder':'Email',
                                }
                                ))
    username = forms.CharField(help_text='',
                                label='',
                                widget=forms.TextInput(attrs={
                                    'class':'username-input',
                                    'placeholder':'Username',
                                }
                                ))
    password1 = forms.CharField(help_text='',
                                label='',
                                widget=forms.PasswordInput(attrs={
                                    'class':'password-input',
                                    'placeholder':'Password',
                                }
                                ))
    password2 = forms.CharField(help_text='',
                                label='',
                                widget=forms.PasswordInput(attrs={
                                    'class':'password-input',
                                    'placeholder':'Enter password again',
                                }
                                ))

    class Meta:
        model=User
        fields = ['username', 'password1', 'password2', 'email']



class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'class':'username-input',
            'placeholder':'Username'
        })
    )

    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={
            'class':'password-input',
            'placeholder':'Password'
        })
    )

        

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
        labels = {
            'title':'',
            'description':'',
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'class':'title-input',
                'placeholder': 'Title',
            }),
            'description': forms.Textarea(attrs={
                'class':'description-input',
                'placeholder': 'Description'
            }),
        }
        
        