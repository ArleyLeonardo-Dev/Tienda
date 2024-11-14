from rest_framework import serializers #importamos serializer de rest_framework
from .models import Productos #importamos la trabla de models


class ProductosSerializer(serializers.ModelSerializer):#creamos un serializer de tipo model
    Tipo = serializers.CharField()#este campo lo defino así pq el campo Tipo fue hecho despues de crear la tabal y con los fields de abajo no me lo reconocia por eso no se encuentra abajo

    class Meta:#le asignamos metadatos
        model = Productos#definimos el modelo con el cual vamos a compara
        fields = ["Nombre","Descripcion","Precio","Cantidad"]#Campos que seran comparados