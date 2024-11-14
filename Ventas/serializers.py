from rest_framework import serializers
from .models import RegistroVentas

class RegistroVentasSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroVentas
        fields = ["Producto", "Cantidad"]