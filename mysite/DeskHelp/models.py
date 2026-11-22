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
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="OPEN")
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


class Comment(models.Model):
    comment = models.CharField(max_length=100, blank=False)
    datetime = models.DateTimeField(auto_now_add=True)

    owner = models.ForeignKey(User, 
                            related_name="comment_owner",
                            on_delete=models.CASCADE,
                            null=True,
                            blank=True)

    ticket = models.ForeignKey(Ticket,
                               related_name="belonging_ticket",
                               on_delete=models.CASCADE,
                               null=True,
                               blank=True)

    def __str__(self):
        return f"{self.id} - {self.comment}"

class Profile(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                related_name='profile',)

    profile_pic = models.ImageField(upload_to='profile_pics/',
                                    default='profile_pics/default.png',
                                    blank=True)

    bio = models.TextField(max_length=150, 
                           blank=True,
                           default='')

    def __str__(self):
        return self.user.username

class Notification(models.Model):
    recipient = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='notification'
    )

    ticket = models.ForeignKey(
        Ticket,
        on_delete=models.CASCADE,
    )

    comment = models.ForeignKey(
        Comment,
        on_delete=models.CASCADE
    )

    read = models.BooleanField(default=False)

    created_at = models.TimeField(auto_now_add=True)