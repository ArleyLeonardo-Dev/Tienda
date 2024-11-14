from django.db import models

# Create your models here.
#creamos la tabla productos
class Productos(models.Model):
    Nombre = models.CharField(max_length=50, unique=True)#campo Nombre en el cual se guardara el nombre de los productos, esta tiene un max_length que define el maximo de caracteres del nombre y un unique que define que en la tabla solo puede haber un nombre, cada nombre es unico

    Descripcion = models.TextField(max_length=500)#campo que describe un producto con su debido max_length

    Precio = models.IntegerField()#campo de tipo entero en el que se define el precio
    
    Tipo = models.CharField(max_length=100, default=" ")#campo donde se define el tipo del producto con su debido max_length y default que define de que si en algun momento este campo no se llena el automaticamente se llenara con lo que le pongas que en este caso es ""

    Cantidad = models.IntegerField()#campo que define la cantidad de productos que hay