from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import forms
from django.contrib.auth.views import LoginView, PasswordResetDoneView, PasswordResetConfirmView,PasswordChangeView, PasswordChangeDoneView, PasswordResetView
from django.urls import reverse_lazy

def home_view(request):
    return render(request,"DeskHelp/index.html")

def signup_view(request):
    if request.method == "POST":
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
        else:
            return HttpResponse("Invalid")
        return redirect('login')
    else:
        form = forms.SignUpForm()
        return render(request, 'DeskHelp/registration/signup.html', {'form':form})

class MyLoginView(LoginView):
    form_class = forms.LoginForm
    template_name = 'DeskHelp/registration/login.html'
    next_page = reverse_lazy('home')

class MyPasswordChangeView(PasswordChangeView):
    form_class = forms.PasswordChangeForm
    template_name = 'DeskHelp/registration/password_change_form.html'

class MyPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'DeskHelp/registration/password_change_done.html'

class MyPasswordResetView(PasswordResetView):
    template_name = 'DeskHelp/registration/password_reset_form.html'
    form_class = forms.MyPasswordResetForm
    success_url = reverse_lazy('password_reset_done')   

class MyPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'DeskHelp/registration/password_reset_done.html'

class MyPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = forms.SetPasswordForm
    template_name = 'DeskHelp/registration/password_reset_confirm.html' 
    success_url = reverse_lazy('login')
