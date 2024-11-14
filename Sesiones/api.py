from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
# Create your views here.

#heredo de token obtain pair view que es la vista predefinidad para obtner tokens
class loggin(TokenObtainPairView):
    def get(self, request): #le agrego el metodo get para que se sepa que introducir
        data = {
            "username":"required",
            "password":"required"
        }
        return Response(data, status.HTTP_200_OK)