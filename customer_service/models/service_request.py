from django.db import models
from .customer import Customer  
from django.utils.timezone import now

class ServiceRequest(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
    ]

    REQUEST_TYPES = [
        ('INSTALLATION', 'Installation'),
        ('REPAIR', 'Repair'),
        ('MAINTENANCE', 'Maintenance'),
    ]   

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE) 
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    request_type = models.CharField(max_length=20, choices=REQUEST_TYPES)
    request_details = models.TextField()
    request_date = models.DateTimeField(auto_now_add=True)
    attachment = models.FileField(upload_to='uploads/', null=True, blank=True)
    resolved_date = models.DateTimeField(null=True, blank=True) 
    
    def save(self, *args, **kwargs):
        if self.status.lower() == 'resolved' and not self.resolved_date:
            self.resolved_date = now()
        elif self.status.lower() != 'resolved':  
            self.resolved_date = None
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.customer.name} - {self.status}"
