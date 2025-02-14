from django.shortcuts import render, redirect, reverse
from .models import *
# import requests as req
# from bs4 import BeautifulSoup as bs
# from datetime import datetime as dt
# from time import timezone
# import requests
# from django.http import JsonResponse
# from rest_framework.decorators import api_view


def about(request):
    """Fetch about information and display it based on visibility settings."""
    about = About.objects.first()  # Fetch the first (and only) entry
    return render(request, 'about.html', {'about': about})
