from rest_framework.response import Response
from rest_framework import status
from Productos.models import Productos
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import RegistroVentasSerializer
# Create your views here.

@api_view(["POST"])#vista con un unico metodo post
@permission_classes([IsAuthenticated])
def HacerVenta(request):
    datos = request.data#ser obtienen los datos del body
    datos["Producto"] = datos["Producto"].lower()#el nombre del producto se pasa a minusculas

    serializer = RegistroVentasSerializer(data = datos)#se verifica que todos los campos del body esten bien

    if serializer.is_valid():#si es valido
        producto = Productos.objects.get(Nombre = datos["Producto"])#se obtiene el producto que se vendio de la tabla productos
        
        if producto.Cantidad == 0:#verifica si el producto que se vendio tiene stock
            return Response({"mssg":[f"No hay stock de {producto.Nombre}"]})
        
        if producto.Cantidad > 0 and producto.Cantidad < datos["Cantidad"]:#si si hay stock, verifica que la cantidad que se va a vender si exista, pueden haber 3 en stock y quieran comprar 4
            return Response({"mssg":["No se puedo concretar la compra", f"{producto.Nombre} disponibles {producto.Cantidad}"]})
        
        #si si hay stock y disponibilidad
        serializer.save()#guarda la venta en la tabla de historial
        producto.Cantidad = producto.Cantidad - datos["Cantidad"]#le resta la cantidad vendida a la cantidad de stock en la tabla productos
        producto.save()#y guarda ese cambio

        #y devuelve la confirmacion de la venta
        return Response({"mssg":[f"Se ah vendido un/a {producto.Nombre}"]}, status.HTTP_200_OK)
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)