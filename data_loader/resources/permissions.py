from rest_framework import permissions

from data_loader.resources.models import UploadedImage


class Permission200px(permissions.BasePermission):

    def has_permission(self, request, view):
        owner = UploadedImage.objects.get(id=view.kwargs.get('pk')).owner
        return request.user.subscribe_plan != 'Out' and (
            request.user == owner
        )


class PermissionExpireLink(permissions.BasePermission):

    def has_permission(self, request, view):
        owner = UploadedImage.objects.get(id=view.kwargs.get('pk')).owner
        return request.user.subscribe_plan == 'Enterprise' and (
            request.user == owner
        )


class Permission400pxAndOriginal(permissions.BasePermission):

    def has_permission(self, request, view):
        owner = UploadedImage.objects.get(id=view.kwargs.get('pk')).owner
        return (request.user.subscribe_plan == 'Enterprise' or (
            request.user.subscribe_plan == 'Premium'
        )) and (request.user == owner)
