from django.contrib import admin
from .models import Employee,SupportStaff,Ticket,Category

admin.site.register(Employee)
admin.site.register(SupportStaff)
admin.site.register(Ticket)
admin.site.register(Category)

# Register your models here.
