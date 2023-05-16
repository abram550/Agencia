from django.urls import path
from Apps.Viajes.views import home

urlpatterns = [
    path('inicio/',home, name = 'home')
]