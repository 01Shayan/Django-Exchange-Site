
from django.contrib import admin
from django.urls import path, include
# from currency import views
# from calculator import views
# from about import views
# from doviz import views


urlpatterns = [
    path('secretadmin/', admin.site.urls),
    path('secretmysql/', include('mysql_app.urls')),
    path('', include('currency.urls')),
    path('', include('calculator.urls')),
    path('', include('about.urls')),
    path('', include('doviz.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
    path('', include('pwa.urls')),
]
