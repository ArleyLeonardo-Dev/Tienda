from django.urls import path
from .api import HacerVenta
urlpatterns = [
    path('', HacerVenta)
]