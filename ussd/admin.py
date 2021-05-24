from django.contrib import admin
# from django.contrib.auth import get_user_model

# User = get_user_model()

# Register your models here.
from .models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    fields = ('id', 'first_name', 'last_name', 'phone_number', 'balance')
    list_display = ('id', 'first_name', 'last_name', 'phone_number', 'balance')
    readonly_fields = ('id',)
    search_fields = ('id', 'first_name', 'last_name', 'phone_number', 'balance')
    list_per_page = 20
