from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from data_loader.users.permissions import IsSelfUser
from data_loader.users.serializers import (
    UserSerializer, SignUpSerializer
)


class SignUpView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    permission_classes = [AllowAny]
    serializer_class = SignUpSerializer


class UsersView(generics.ListAPIView):
    queryset = get_user_model().objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer


class UserView(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    permission_classes = [IsAuthenticated, IsSelfUser]
    serializer_class = UserSerializer
    lookup_field = 'pk'
