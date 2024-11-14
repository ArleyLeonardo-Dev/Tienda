from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('productos/', include('Productos.urls')),#inicio de urls para los endpoint de productos
    path('sesion/', include('Sesiones.urls')),#inicio de urls para los endpoint de sesiones
    path('Ventas/', include('Ventas.urls')),#inicio de urls para los endpoint de ventas,
    path('HelloWorld/', include('HelloWorld.urls'))
]
