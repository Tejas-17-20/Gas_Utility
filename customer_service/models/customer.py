from django.db import models
import datetime

class Customer(models.Model):
    customer_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)  
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name
