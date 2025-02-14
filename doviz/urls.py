
from django.urls import path
from . import views

app_name = 'doviz'
urlpatterns = [
    path('doviz', views.doviz, name='doviz'),
]
