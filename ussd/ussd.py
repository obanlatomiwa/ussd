import os
import requests
from django.conf import settings
from .models import Customer
from django.views.decorators.http import require_POST
from django.http import HttpResponse, Http404, HttpResponseNotFound


def ussd(request):
    # Read the variables sent via POST from our API

    if request.method == "POST":
        session_id = request.values.get("sessionId", None)
        serviceCode = request.values.get("serviceCode", None)
        phone_number = request.values.get("phoneNumber", None)
        text = request.values.get("text", "default")

        current_user = Customer.objects.get(phone_number=phone_number)

        if current_user:
            if text == '':
                # This is the first request. Note how we start the response with CON
                response = "CON What would you want to check \n"
                response += "1. My Account Balance \n"
                response += "2. Loan"

            elif text == '1':
                # Business logic for first level response
                balance = current_user.balance

                response = "END Your Account Balance is" + balance

            elif text == '2':
                # This is a terminal request. Note how we start the response with END
                response = "CON Your phone number is "

            else:
                response = "END Invalid choice"

        else:
            if text == '':
                # This is the first request. Note how we start the response with CON
                response = "CON Welcome to Cashcard \n"
                response += "1. Create Your Account \n"
                response += "2. Exit"

            elif text == '1':
                # Business logic for first level response
                response = "CON Enter your first_name \n"

            elif text == '2':
                # This is a terminal request. Note how we start the response with END
                response = "END Good luck"

            else:
                response = "END Invalid choice"

        # Send the response back to the API
        return response
