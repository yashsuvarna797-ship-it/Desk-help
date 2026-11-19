from django.contrib import admin
from .models import SupportStaff,Ticket,Category,Comment,Profile

admin.site.register(SupportStaff)
admin.site.register(Ticket)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Profile)


# Register your models here.
