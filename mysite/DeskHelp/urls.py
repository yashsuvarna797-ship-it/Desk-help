from django.urls import path
from . import views

urlpatterns=[
    path('', views.home_view, name='home'),
    path('Signup', views.signup_view, name='signup'),
    path('Login', views.MyLoginView.as_view(), name='login'),

]