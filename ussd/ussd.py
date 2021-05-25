import os
import requests
from django.conf import settings
from .models import Customer, Loan
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import HttpResponse, Http404, HttpResponseNotFound


@csrf_exempt
@require_POST
def ussd_main(request):
    # Read the variables sent via POST from our API

    if request.method == "POST":
        print(request.POST)
        session_id = request.POST.get("sessionId", None)
        serviceCode = request.POST.get("serviceCode", None)
        phone_number = request.POST.get("phoneNumber", None)
        text = request.POST.get("text", " ")

        try:
            current_user = Customer.objects.get(phone_number=phone_number)
        except Customer.DoesNotExist:
            current_user = None

        data = text.split('*')

        if current_user:
            if text == '':
                # This is the first request. Note how we start the response with CON
                response = "CON What would you want to check \n"
                response += "1. My Account Balance \n"
                response += "2. Loan"
                return HttpResponse(response)

            elif data[0] == '1' and len(data) == 1:
                # Business logic for first level response
                response = "END Your Account Balance is " + str(current_user.balance)
                return HttpResponse(response)

            elif data[0] == '2':
                if data[0] == '2' and len(data) == 1:
                    response = "CON Your Loan Application \n"
                    response += "1. Start Loan Application \n"
                    response += "2. Exit"
                    return HttpResponse(response)

                elif data[1] == '1' and len(data) == 2:
                    if len(data) == 2:
                        response = "CON Enter your bvn \n"
                        return HttpResponse(response)
                    elif len(data) == 3:
                        response = "CON Enter Loan Amount \n"
                        return HttpResponse(response)
                    elif len(data) == 4:
                        response = "CON Enter Return Date in the format day/month/year \n"
                        return HttpResponse(response)
                    elif len(data) == 5:
                        response = "END Your Loan application has been sent, and it's under verification." \
                                   " You will get a SMS if successful \n"

                        bvn, loan_amount, return_date, loaner = data[2], data[3], data[4], current_user.id
                        Loan.objects.create(loaner=loaner, bvn=bvn, return_date=return_date, loan_amount=loan_amount)
                        return HttpResponse(response)

            # elif data[0] == '2' and len(data) == 2:
            #     loan_amount = data[1]
            #     response = "END Your Loan of " + loan_amount + " has been accepted."
            #     return HttpResponse(response)

            else:
                response = "END Invalid choice"
                return HttpResponse(response)

        else:
            if text == '':
                # This is the first request. Note how we start the response with CON
                response = "CON Welcome to Cashcard \n"
                response += "1. Create Your Account \n"
                response += "2. Exit"
                return HttpResponse(response)

            elif data[0] == '1':
                if len(data) == 1:
                    response = "CON Enter your first_name \n"
                    return HttpResponse(response)
                elif len(data) == 2:
                    response = "CON Enter your surname \n"
                    return HttpResponse(response)
                elif len(data) == 3:
                    response = "END Your account " + phone_number + " has been created."
                    first_name, surname = data[1], data[2]
                    Customer.objects.create(first_name=first_name, last_name=surname, phone_number=phone_number,
                                            balance=0.00)
                    return HttpResponse(response)

            elif data[0] == '2':
                # This is a terminal request. Note how we start the response with END
                response = "END Good luck"
                return HttpResponse(response)

            else:
                response = "END Invalid choice"
                return HttpResponse(response)

    else:
        return HttpResponse('Your are not using a post request')
