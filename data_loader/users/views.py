from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from data_loader.users.models import User
from data_loader.users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
