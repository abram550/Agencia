from django.urls import path
from Apps.Viajeros.views import home

urlpatterns = [
    path('inicio/',home, name = 'home')
]