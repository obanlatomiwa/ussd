import os
import requests
from django.conf import settings
from .models import Customer
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import HttpResponse, Http404, HttpResponseNotFound


@csrf_exempt
@require_POST
def ussd_main(request):
    # Read the variables sent via POST from our API

    if request.method == "POST":
        session_id = request.values.get("sessionId", None)
        serviceCode = request.values.get("serviceCode", None)
        phone_number = request.values.get("phoneNumber", None)
        text = request.values.get("text", " ")

        current_user = Customer.objects.get(phone_number=phone_number)
        data = text.split('*')

        if current_user:
            if text == '':
                # This is the first request. Note how we start the response with CON
                response = "CON What would you want to check \n"
                response += "1. My Account Balance \n"
                response += "2. Loan"
                return HttpResponse(response)

            elif data[0] == '1':
                # Business logic for first level response
                response = "END Your Account Balance is" + balance
                return HttpResponse(response)

            elif data[0] == '2':
                response = "CON How much Loan do you need \n"
                response += "END Your Loan of " + data[1] + " has been accepted."

                return HttpResponse(response)

            else:
                response = "END Invalid choice"
                return HttpResponse(response)

        else:
            if text == '':
                # This is the first request. Note how we start the response with CON
                response = "CON Welcome to Cashcard \n"
                response += "1. Create Your Account \n"
                response += "2. Exit"

            elif data[0] == '1':
                # Business logic for first level response
                response = "CON Enter your first_name \n"
                response += "Enter your surname \n"
                first_name, surname = data[1], data[2]
                Customer.objects.create(first_name=first_name, last_name=surname, phone_number=phone_number,
                                        balance=0.00)

                response = "END Your account with " + phone_number + "has been created."
                return HttpResponse(response)

            elif data[0] == '2':
                # This is a terminal request. Note how we start the response with END
                response = "END Good luck"
                return HttpResponse(response)

            else:
                response = "END Invalid choice"
                return HttpResponse(response)

        # Send the response back to the API
        return HttpResponse(response)

    else:
        return HttpResponse('Your are not using a post request')
