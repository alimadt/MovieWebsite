from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import MyUser
from .serializers import RegisterSerializer
from .utils import send_activation_code


class RegisterView(APIView):
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response("You have successfully registered", status=status.HTTP_201_CREATED)


class ActivationView(APIView):
    def get(self, request, email, activation_code):
        user = MyUser.objects.get(email=email, activation_code=activation_code)
        if not user:
            return Response('User was not found', status=status.HTTP_400_BAD_REQUEST)
        user.activation_code = ''
        user.is_active = True
        user.save()
        return Response('User was activated', status=status.HTTP_200_OK)


# class LoginView(ObtainAuthToken):
#     serializer_class = LoginSerializer
#
#
# class LogoutView(APIView):
#     permission_classes = [IsAuthenticated, ]
#
#     def post(self, request):
#         user = request.user
#         Token.objects.filter(user=user).delete()
#         return Response('You have logged out', status=status.HTTP_200_OK)


