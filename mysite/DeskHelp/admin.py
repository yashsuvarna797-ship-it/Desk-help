from django.contrib import admin
from .models import Employee,SupportStaff,Ticket

admin.site.register(Employee)
admin.site.register(SupportStaff)
admin.site.register(Ticket)

# Register your models here.
