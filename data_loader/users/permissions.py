from rest_framework import permissions
from django.contrib.auth import get_user_model


class IsSelfUser(permissions.BasePermission):

    def has_permission(self, request, view):
        user = get_user_model().objects.get(id=view.kwargs.get('pk'))
        return request.user == user
