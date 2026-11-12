from django.shortcuts import render
from django.http import HttpResponse
from . import forms

def home_view(request):
    return render(request,"DeskHelp/index.html")

def signup_view(request):
    if request.method == "POST":
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            return render(request, 'HelpDesk/Auth/login.html')
        else:
            return HttpResponse("Invalid")
    else:
        form = forms.SignUpForm()
        return render(request, 'DeskHelp/Auth/signup.html', {'form':form})