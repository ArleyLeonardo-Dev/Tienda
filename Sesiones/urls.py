from django.urls import path
from .api import loggin

urlpatterns = [
    path("loggin/", loggin.as_view())#aqui le doy el endpoint para hacer llamado a la vista para obtener los tokens
]