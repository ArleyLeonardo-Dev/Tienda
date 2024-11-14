from django.db import models
from Productos.models import Productos #importamos la tabla de productos para vincular esta tabla con la de productos 

# Create your models here.
class RegistroVentas(models.Model):
    Producto = models.ForeignKey(to=Productos, on_delete=models.CASCADE,to_field="Nombre", unique=False)#el campo producto guardara el prducto que se vendio, siendo este campo una llave foranea, el to="", es donde se le dice la tabla que se va a vincular, on delete= hace referencia que pasa si el registro de la tabla productos se borra popr lo que aqui se define que apenas se elimine el registro, se elimaran todos los registros vinculadas al registro eliminado, por defecto se vincula el id de la tabal principal, con to_field se puede definir que campo se va a vicular, en este caso sera el campo nombre de la tabla productos, unique= si esta en true lo que hara es que el registro sea unico, esta enb false para evitar problemas 
    Cantidad = models.IntegerField()#campo que almacenara la cantidad que se vendio
    Hora = models.DateTimeField(auto_now=True)#campo de tipo fecha y hora con auto_now= para que apenas se cree un registro este se autollene con la hora y fecha en la que se creó
