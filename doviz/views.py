from django.shortcuts import render, redirect, reverse
from .models import *
import requests as req
from bs4 import BeautifulSoup as bs
from datetime import datetime as dt
from time import timezone
import requests
from django.http import JsonResponse
from rest_framework.decorators import api_view



def doviz(request):

    today = dt.today().strftime("%d %B %Y (%A)")
    time = dt.today().strftime("%H:%M")

    url = "http://www.sakaryadoviz.com.tr/"
    result = req.get(url).text
    soup = bs(result)

    usd_rate_1 = soup.find_all("td")[2].text
    usd_b_rate = float(usd_rate_1)
    usd_rate_2 = soup.find_all("td")[3].text
    usd_s_rate = float(usd_rate_2)

    eur_rate_1 = soup.find_all("td")[6].text
    eur_b_rate = float(eur_rate_1)
    eur_rate_2 = soup.find_all("td")[7].text
    eur_s_rate = float(eur_rate_2)

    gbp_rate_1 = soup.find_all("td")[10].text
    gbp_b_rate = float(gbp_rate_1)
    gbp_rate_2 = soup.find_all("td")[11].text
    gbp_s_rate = float(gbp_rate_2)

    cad_rate_1 = soup.find_all("td")[42].text
    cad_b_rate = float(cad_rate_1)
    cad_rate_2 = soup.find_all("td")[43].text
    cad_s_rate = float(cad_rate_2)

    aud_rate_1 = soup.find_all("td")[22].text
    aud_b_rate = float(aud_rate_1)
    aud_rate_2 = soup.find_all("td")[23].text
    aud_s_rate = float(aud_rate_2)

    irt_b_rate = 1.185
    irt_s_rate = 1.191

    try_b_rate = 2.22
    try_s_rate = 2.23

    sar_rate_1 = soup.find_all("td")[18].text
    sar_b_rate = float(sar_rate_1)
    sar_rate_2 = soup.find_all("td")[19].text
    sar_s_rate = float(sar_rate_2)

    jpy_rate_1 = soup.find_all("td")[38].text
    jpy_b_rate = float(jpy_rate_1)
    jpy_rate_2 = soup.find_all("td")[39].text
    jpy_s_rate = float(jpy_rate_2)

    chf_rate_1 = soup.find_all("td")[14].text
    chf_b_rate = float(chf_rate_1)
    chf_rate_2 = soup.find_all("td")[15].text
    chf_s_rate = float(chf_rate_2)

    dkk_rate_1 = soup.find_all("td")[26].text
    dkk_b_rate = float(dkk_rate_1)
    dkk_rate_2 = soup.find_all("td")[27].text
    dkk_s_rate = float(dkk_rate_2)

    sek_rate_1 = soup.find_all("td")[30].text
    sek_b_rate = float(sek_rate_1)
    sek_rate_2 = soup.find_all("td")[31].text
    sek_s_rate = float(sek_rate_2)

    nok_rate_1 = soup.find_all("td")[34].text
    nok_b_rate = float(nok_rate_1)
    nok_rate_2 = soup.find_all("td")[35].text
    nok_s_rate = float(nok_rate_2)

    context = { 
        'today': today,
        'time': time,

        'usd_b_rate': usd_b_rate,
        'eur_b_rate': eur_b_rate,
        'try_b_rate': try_b_rate,
        'irt_b_rate': irt_b_rate,
        'gbp_b_rate': gbp_b_rate,
        'chf_b_rate': chf_b_rate,
        'sar_b_rate': sar_b_rate,
        'aud_b_rate': aud_b_rate,
        'cad_b_rate': cad_b_rate,
        'jpy_b_rate': jpy_b_rate,
        'sek_b_rate': sek_b_rate,
        'dkk_b_rate': dkk_b_rate,
        'nok_b_rate': nok_b_rate,

        'usd_s_rate': usd_s_rate,
        'eur_s_rate': eur_s_rate,
        'try_s_rate': try_s_rate,
        'irt_s_rate': irt_s_rate,
        'gbp_s_rate': gbp_s_rate,
        'chf_s_rate': chf_s_rate,
        'sar_s_rate': sar_s_rate,
        'aud_s_rate': aud_s_rate,
        'cad_s_rate': cad_s_rate,
        'jpy_s_rate': jpy_s_rate,
        'sek_s_rate': sek_s_rate,
        'dkk_s_rate': dkk_s_rate,
        'nok_s_rate': nok_s_rate,
    }

    return render(request, 'doviz.html', context)
