
from django.urls import path
from . import views

app_name = 'calculator'
urlpatterns = [
    path('calculator', views.calculator, name='calculator'),
]
