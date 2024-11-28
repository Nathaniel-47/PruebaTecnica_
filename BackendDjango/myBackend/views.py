from rest_framework import viewsets, generics
from .models import User
from .serializers import UserSerializer
from rest_framework.views import APIView 
from django.core.mail import send_mail 
from django.conf import settings
from rest_framework import status 
from rest_framework.response import Response 
from django.contrib.auth.models import User
import random 
from django.contrib.auth.models import User



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class VerifyEmailView(APIView): 
    def post(self, request, *args, **kwargs): 
        email = request.data.get('email') 
        # Lógica para enviar correo de verificación
        send_mail( 'Verificación de Email',
                'Por favor, verifica tu email haciendo clic en el siguiente enlace...', settings.DEFAULT_FROM_EMAIL,
                [email], ) 
        return Response({'message': 'Correo de verificación enviado'})

class GenerateWinnerView(APIView): 
    def get(self, request, *args, **kwargs): 
        users = User.objects.all() 
        winner = random.choice(users) 
        # Lógica para enviar correo de notificación al ganador 
        send_mail( '¡Felicidades!',
                f'Has ganado el sorteo, {winner.name}!', 
                settings.DEFAULT_FROM_EMAIL,
                [winner.email], ) 
        return Response({'message': f'El ganador es {winner.name}'})
    


class SetPasswordView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        user = User.objects.get(email=email)
        user.set_password(password)
        user.save()
        return Response({'message': 'Contraseña asignada con éxito'}, status=200)

    
