from django.db import models
from django.contrib.auth.models import User



class SupportStaff(models.Model):
    name = models.CharField(max_length=40, blank=False)
    email = models.EmailField(max_length=50, blank=False)

    owner = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return f"{self.id} - {self.name}"

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description=models.TextField(blank=True)

    def __str__(self):
        return f"{self.id} - {self.name}"

class Ticket(models.Model):
    STATUS_CHOICES = [
        ("OPEN","open"),
        ("IN_PROGRESS","In Progress"),
        ("RESOLVED", "Resolved"),
        ("CLOSED", "Closed"),
    ]

    title = models.CharField(max_length=40, blank=False)
    description=models.TextField(max_length=500, blank=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="OPEN", editable=False)
    datetime = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category,
                                on_delete=models.PROTECT,
                                related_name="tickets",
                                null=True,
                                blank=True)
    owner = models.ForeignKey(User,
                              related_name="ticket_owner",
                              on_delete=models.CASCADE,
                              null=True,
                              blank=True)
    assigned_staff = models.ForeignKey(SupportStaff,
                                       related_name="assigned_tickets",
                                       on_delete = models.SET_NULL,
                                       null=True,
                                       blank=True)
    
    def __str__(self):
        return f"{self.id} - {self.title}"

