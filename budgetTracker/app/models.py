from django.db import models
from django.contrib.auth.models import User, AbstractUser, AbstractBaseUser
from django.conf import settings

# Create your models here.


class CustomUser(AbstractUser):
    pass


# Pre defined category
CATEGORY_CHOICES = [
    ('Food', 'Food'),
    ('Utilities', 'Utilities'),
    ('Transport', 'Transport'),
    ('Entertainment', 'Entertainment'),
    ('Health', 'Health'),
    ('Other', 'Other')
]



class Income(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    source = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)


class Expense(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    description = models.TextField(blank=True)

    # Predefined category    
    category = models.CharField(max_length=15, choices=CATEGORY_CHOICES)
    

class Budget(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Predefined category    
    category = models.CharField(max_length=15, choices=CATEGORY_CHOICES)



class Notification(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)