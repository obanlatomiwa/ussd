from django.contrib import admin
# from django.contrib.auth import get_user_model

# User = get_user_model()

# Register your models here.
from .models import Customer, Loan


@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    fields = ('id', 'loaner', 'created', 'bvn', 'return_date', 'loan_amount')
    list_display = ('id', 'loaner', 'created', 'bvn', 'return_date', 'loan_amount')
    readonly_fields = ('id',)
    search_fields = ('id', 'loaner', 'created', 'bvn')
    list_per_page = 20


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    fields = ('id', 'first_name', 'last_name', 'phone_number', 'balance')
    list_display = ('id', 'first_name', 'last_name', 'phone_number', 'balance')
    readonly_fields = ('id',)
    search_fields = ('id', 'first_name', 'last_name', 'phone_number', 'balance')
    list_per_page = 20
