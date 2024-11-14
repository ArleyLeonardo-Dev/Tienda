from django.urls import path
from .api import ProdcutosViews, productfiltertype, productfilterstock,productfilternotstock

urlpatterns = [
    path('', ProdcutosViews.as_view()),#hay dos urls que llaman a la misma clase pq los unicos metodos que hacen uso de la variable por url es el metodo get, patch y delete, por lo que los metodos post y el mismo metodo get hacen uso de este path
    path('<str:name>', ProdcutosViews.as_view()),#y el metodo get, patch y delete hace uso de este path y su variable
    path('filter/type/<str:tipo>', productfiltertype),
    path('filter/stock/aviable/', productfilterstock),
    path('filter/stock/notaviable/', productfilternotstock)
]