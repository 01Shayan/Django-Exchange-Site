from django.shortcuts import render, redirect, reverse
from .models import *
from datetime import datetime as dt
# import requests as req
# from bs4 import BeautifulSoup as bs
# from time import timezone
# import requests
# from django.http import JsonResponse
# from rest_framework.decorators import api_view


def index(request):
    
    today = dt.today().strftime("%d %B %Y (%A)")
    time = dt.today().strftime("%H:%M")

    """Display buy and sell rates for active currencies."""
    currencies = Currency.objects.filter(is_active=True).order_by('order')  # Show only active currencies
    config = Configuration.objects.first()  # Get the first (and only) configuration entry

    context = {
        'currencies': currencies,
        'prices_fee': config.prices_fee if config else 0,
        'show_prices_fee': config.show_prices_fee if config else False,
        'today': today,
        'time': time,
        }

    return render(request, 'index.html', context)


# from time import timezone

# import requests as req
# from bs4 import BeautifulSoup as bs
# from django.shortcuts import render
# from datetime import datetime as dt


# def currency(request):
#     # Get the selected origin currency, default to 'TRY'
#     origin_currency = request.GET.get('origin_currency', 'USD')
#     # print(f"Selected Origin Currency: {origin_currency}")  # Debug

#     # Fetch exchange rates
#     API_URL = f"https://v6.exchangerate-api.com/v6/780ebc448a9d8983cd5809c9/latest/{origin_currency}"
#     today = dt.today().strftime("%A %m %-Y")
#     time = dt.today().strftime("%H:%M:%S")



#     web = "http://www.sakaryadoviz.com.tr/"
#     res = req.get(web).text
#     soup = bs(res)

#     usd_rate_1 = soup.find_all("td")[2].text
#     usd_b_rate = float(usd_rate_1)
#     usd_rate_2 = soup.find_all("td")[3].text
#     usd_s_rate = float(usd_rate_2)

#     eur_rate_1 = soup.find_all("td")[6].text
#     eur_b_rate = float(eur_rate_1)
#     eur_rate_2 = soup.find_all("td")[7].text
#     eur_s_rate = float(eur_rate_2)

#     try_b_rate = 2.22
#     try_s_rate = 2.23

#     irt_b_rate = 2.22
#     irt_s_rate = 2.23




#     try:
#         response = req.get(API_URL)
#         data = response.json()

#         # usd_rate = 78
#         eur_rate = 1000
#         try_rate = 1000
#         irr_rate = 1000
#         origin_currency = origin_currency


#     except Exception as e:
#         print(f"API Error: {e}")
#         data = {'rates': {}}

#     return render(request, 'currency.html', {
#         'today': today,
#         'time': time,
#         'origin_currency': origin_currency,

#         # 'amount': amount,

#         # 'usd_price': usd_price,
#         # 'eur_price': eur_price,
#         # 'try_price': try_price,
#         # 'irr_price': irr_price,

#         # 'usd_rate': usd_rate,
#         # 'eur_rate': eur_rate,
#         # 'try_rate': try_rate,
#         # 'irr_rate': irr_rate,


#         'usd_b_rate': usd_b_rate,
#         'eur_b_rate': eur_b_rate,
#         'try_b_rate': try_b_rate,
#         'irt_b_rate': irt_b_rate,

#         'usd_s_rate': usd_s_rate,
#         'eur_s_rate': eur_s_rate,
#         'try_s_rate': try_s_rate,
#         'irt_s_rate': irt_s_rate,

#     })


#     # Process rates
#     # rates = []
#     # for code, rate in data.get('rates', {}).items():
#     #     rates.append({
#     #         'code': code,
#     #         'buy_rate': rate * 0.98,  # Example: 2% lower for buy rate
#     #         'sell_rate': rate * 1.02,  # Example: 2% higher for sell rate
#     #     })
#     #


# # from django.shortcuts import render
# # import requests
# #
# # def home(request):
# #     origin_currency = request.GET.get('origin_currency')  # Default is TRY
# #     API_URL = f"https://api.exchangerate-api.com/v4/latest/{origin_currency}"
# #     response = requests.get(API_URL)
# #     data = response.json()
# #
# #     rates = []
# #     for code, rate in data['rates'].items():
# #         rates.append({
# #             'code': code,
# #             'rate': rate
# #         })
# #
# #     return render(request, 'currency/home.html', {
# #         'origin_currency': origin_currency,
# #         'rates': rates,
# #     })



# def last(request):
    
    


#     return render(request, 'currency.html', {
        

#     })
