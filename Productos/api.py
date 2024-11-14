from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Productos
from .serializers import ProductosSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class ProdcutosViews(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, name = ""):#en este metodo get el atributo name esta "name = "" y es pq si el usuario no manda ninguna variable no se caiga el programa"
        
        if name == "":#aqui se verifica si el usuario mando algo por la url, en este caso el usuario no mando nada pq name es igual a ""
            productos = Productos.objects.all().values()#se obtienen todos los productos llamando a los objetos y haciendo uso del metodo all() para obtener todos
            return Response(productos, status.HTTP_200_OK)#y se retorna
        else:
            name = name.lower()#en el caso contrario donde el usuario si mando el nombre del producto este se pasa a minusculas
            productos = Productos.objects.filter(Nombre = name)#se busca en la tabla
            if not productos:#si no esta devuelve que no
                return Response({"mssg":["Producto no existe"]}, status.HTTP_400_BAD_REQUEST)
            
            return Response(productos.values(), status.HTTP_200_OK)#y si si esta lo devuelve al user

    def post(self, request):#en el metodo post se recojen los datos del producto para crearlo
        data = request.data#se recojen los datos del body
        data["Nombre"] = data["Nombre"].lower()#se pasa el nombre a minusculas

        serializer = ProductosSerializer(data = data)#se le pasan los datos al serializer para que el verifique si los datos estan bien escritos y que encima no exista ya un producto con ese nombre

        if serializer.is_valid():#si es el serializer dice que todo esta bien
            serializer.save()#lo guarda en la tabla
            return Response({"message":["Product Created"]}, status.HTTP_200_OK)#y lo devuelve

        return Response(serializer.errors, status.HTTP_200_OK)#del caso contrario devuelve los errores

    def patch(self, request, name):#el metodo patch actualizara un producto que este en la tabla, este pide el nombre del producto por la URL por lo que este hara uso de la url con la variable

        data = request.data#se recojen los datos del body
        atrib = ["Nombre", "Descripcion", "Precio", "Tipo", "Cantidad"]#una lista con todos los campos de la tabla
        lista = []#y una lista que se utilizara mas tarde

        try:#intentara obtener el producto con su nombre
            producto = Productos.objects.get(Nombre = name)
        except:#si no se puede esta maracarra error y se devolvera que ese producto no existe
            return Response({"message":["Este producto no existe"]}, status.HTTP_400_BAD_REQUEST)

        
        for x in atrib:#este for recorrera la lista de los campos de la tabla
            try:
                if x in data or data[x] != "":#verifica si el primer campo esta en el body o si ese campo este lleno
                    setattr(producto, x, data[x])#del producto obtenido cambiara el campo x por lo que se mando en el body
                    producto.save()#se guardara
                    lista.append(x)#y se añadira el campo que se actualizo a la lista
            except:#si el campo no esta en el body este simplemente continuara y pasara al siguiente campo
                pass

        msg = {
            "Campos actualizados":lista
        }
        return Response(msg, status.HTTP_200_OK)#devolvera al usuario la confirmacion y los campos actualizados

        #este for puede ser complicado pq todo se basa en el x, pero X recorre la lista de los campos por lo que x en la primera vuelta sera x por lo que la sintaxis dentro del for quedaria asi

        """
            if Nombre in data or data["Nombre] != "":
                setattr(producto, "Nombre", data["Nombre"])
                producto.save()
                lista.append("Nombre)
        """          
        #y en la segunda vuelta quedaria tal que
        """
            if Descripcion in data or data["Descripcion] != "":
                setattr(producto, "Descripcion", data["Descripcion"])
                producto.save()
                lista.append("Descripcion)
        """      
        #el setattr lo que hace es cambiar el atributo de un objeto y la sintaxis de el seria tal que "del objeto producto, cambia el campo "Nombre", por lo siguiente "
        #   setattr(producto,     "Nombre",                data["Nombre"])

    def delete(self, request, name):#Este tomara el nombre de la url y eliminara el producto con ese nombre

        
        try:#intenta buscar el producto en la tabla y si no lo encuentra devuelve el error
            producto = Productos.objects.get(Nombre = name)
        except:
            return Response({"message":["Este producto no existe"]}, status.HTTP_400_BAD_REQUEST)
        
        producto.delete()#y elimina el producto, devolviendo que el producto se elimino

        return Response({"message":["Producto eliminado"]}, status.HTTP_200_OK)
    
@api_view(["GET"])#decorador Api_view
@permission_classes([IsAuthenticated])
def productfiltertype(request, tipo):#una vista basada en funciones con el decorador que hace que sea un api_view, lo que hace esta es obtener los productos dependiendo de su tipo

    productos = Productos.objects.filter(Tipo = tipo).values() #obtiene todos los productos que tengan el tipo pasado por URL

    if not productos:
        return Response({"mssg":["Este tipo no existe"]}, status.HTTP_400_BAD_REQUEST)#marca error su no existe
    
    return Response(productos, status.HTTP_200_OK)#devuelve los productos obtenidos

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def productfilterstock(request):#esta vista lo que hace es obtener los productos que si esten en stock osea que su cantidad en la base de datos sea mayor a cero
    productos = Productos.objects.filter(Cantidad__gt = 0).values()#obtiene de la tabla productos los productos que su cantidad sea mayor a cero, esto se hace gracias a "__gt" que esta despues de "cantidad". "__gt" es el comparador "mayor que" y el "__lt" es el comparador menor que

    if not productos:#si no hay productos en stock le devuelve ese evento al user
        return Response({"mssg":["No hay productos en stock"]}, status.HTTP_200_OK)
    return Response(productos, status.HTTP_200_OK)#si si hay, devuelve los productos al user

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def productfilternotstock(request):#esta vista obtiene los productos que no tengan stock, osea que el campo cantidad este en 0
    productos = Productos.objects.filter(Cantidad = 0).values()

    if not productos:
        return Response({"mssg":["No hay productos sin stock"]}, status.HTTP_200_OK)
    
    return Response(productos, status.HTTP_200_OK)