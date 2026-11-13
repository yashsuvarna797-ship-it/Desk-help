from django.urls import path
from . import views

urlpatterns=[
    path('', views.home_view, name='home'),
    path('Signup', views.signup_view, name='signup'),
    path('Login', views.MyLoginView.as_view(), name='login'),
    path('Logout', views.logout_view, name='logout'),
    path('PasswordChange', views.MyPasswordChangeView.as_view(), name='password_change'),
    path('PasswordChangeDone', views.MyPasswordChangeDoneView.as_view(), name='password_change_done'),
    path('PasswordReset', views.MyPasswordResetView.as_view(), name='password_reset'),
    path('PasswordResetDone', views.MyPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('PasswordResetConfirm/<uidb64>/<token>', views.MyPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('CreateTicket', views.CreateTicketView.as_view(), name='create_ticket'),
    path('DisplayTickets', views.display_tickets_view, name='display_tickets'),
    path('DisplayTicketInfo/<int:pk>/', views.display_ticket_info_view, name='display_ticket_info'),
    path('DeleteTicket/<int:pk>/', views.delete_ticket_view, name='delete_ticket'),
    path('UpdateTicket/<int:pk>/', views.UpdateTicketView.as_view(), name='update_ticket'),
    

]