from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.conf import settings


# Create your models here.
class Customer(models.Model):
    # user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    balance = models.DecimalField(max_digits=30, decimal_places=2, default=0)
    phone_number = models.CharField(max_length=20, unique=True)

    class Meta:
        ordering = ['created']
        verbose_name = 'customer'
        verbose_name_plural = 'customers'

    def __str__(self):
        return self.first_name


class Loan(models.Model):
    loaner = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    bvn = models.CharField(max_length=30)
    return_date = models.CharField(max_length=30)
    loan_amount = models.DecimalField(max_digits=30, decimal_places=2, default=0)

    class Meta:
        ordering = ['created']
        verbose_name = 'loan'
        verbose_name_plural = 'loans'

    def __str__(self):
        return self.first_name
