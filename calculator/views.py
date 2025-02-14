from django.shortcuts import render, redirect, reverse
from .models import *
import requests
# import requests as req
# from bs4 import BeautifulSoup as bs
# from datetime import datetime as dt
# from time import timezone
# from django.http import JsonResponse
# from rest_framework.decorators import api_view


API_URL = "https://api.exchangerate-api.com/v4/latest/USD"

def calculator(request):
    """Render the conversion page."""
    if request.method == 'GET':
        return render(request, 'calculator.html')
    elif request.method == 'POST':
        try:
            from_currency = request.POST.get('from', 'USD')
            to_currency = request.POST.get('to', 'USD')
            amount = float(request.POST.get('amount', 1))

            response = requests.get(API_URL)
            if response.status_code != 200:
                return render(request, 'calculator.html', {'error': 'Unable to fetch exchange rates'})

            rates = response.json().get('rates', {})
            if from_currency not in rates or to_currency not in rates:
                return render(request, 'calculator.html', {'error': 'Invalid currency code'})

            converted_amount = amount * (rates[to_currency] / rates[from_currency])
            return render(request, 'calculator.html', {
                'result': f'{amount} {from_currency} = {round(converted_amount, 2)} {to_currency}',
                'from_currency': from_currency,
                'to_currency': to_currency,
                'amount': amount,
                'currencies': rates.keys()
            })
        except Exception as e:
            return render(request, 'calculator.html', {'error': str(e)})
