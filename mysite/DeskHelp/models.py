from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=40, blank=False)
    email = models.EmailField(max_length=50, blank=False)
    employee_id = models.CharField(max_length=8, blank=False, unique=True)

    def __str__(self):
        return f"{self.id} - {self.name}"

class SupportStaff(models.Model):
    name = models.CharField(max_length=40, blank=False)
    email = models.EmailField(max_length=50, blank=False)
    staff_id = models.CharField(max_length=8, blank=False, unique=True)

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
    type = models.CharField(max_length=40, blank=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="OPEN")
    datetime = models.DateTimeField()

    owner = models.ForeignKey(Employee,
                             on_delete=models.CASCADE,
                             related_name="created_tickets",
                             blank=False,
                             null=False)
    assigned_staff = models.ForeignKey(SupportStaff,
                                       related_name="assigned_tickets",
                                       on_delete = models.SET_NULL,
                                       null=True,
                                       blank=True)
    
    def __str__(self):
        return f"{self.id} - {self.title}"