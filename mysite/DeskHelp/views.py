from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import forms
from django.contrib.auth.views import LoginView
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