from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

from data_loader.resources.mixins import ThumbnailMixin, ImageMixin
from data_loader.resources.models import UploadedImage
from data_loader.resources.permissions import (
    PermissionExpireLink, Permission400pxAndOriginal, Permission200px
)
from data_loader.resources.serializers import ImageSerializer


class ImageUploadView(ListAPIView):
    queryset = UploadedImage.objects.all()
    serializer_class = ImageSerializer
    parser_classes = [MultiPartParser]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        file = request.FILES['image']
        UploadedImage.objects.create(image=file, owner=request.user)
        return Response(status=200)


class Thumbnail200View(ThumbnailMixin, ListAPIView):
    permission_classes = [Permission200px]
    size = 200, 200


class Thumbnail400View(ThumbnailMixin, ListAPIView):
    permission_classes = [Permission400pxAndOriginal]
    size = 400, 400


class OriginalImageView(ImageMixin, ListAPIView):
    permission_classes = [Permission400pxAndOriginal]
