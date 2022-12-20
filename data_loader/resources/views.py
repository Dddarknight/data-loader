import random
import string
from datetime import datetime, timedelta
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone

from data_loader.resources.mixins import ThumbnailMixin, ImageMixin
from data_loader.resources.models import UploadedImage, ExpiringLink
from data_loader.resources.permissions import (
    PermissionExpireLink, Permission400pxAndOriginal, Permission200px
)
from data_loader.resources.serializers import ImageSerializer


LINK_LENGTH = 20
LINK_EXPIRED = 'You link has expired'


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


class ExpiringLinkView(APIView):
    permission_classes = [PermissionExpireLink]

    def get(self, request, pk, expiring_time=300):
        sequence = string.ascii_lowercase
        url_str = ''.join(random.sample(sequence, LINK_LENGTH))
        ExpiringLink.objects.create(
            url_str=url_str,
            image=UploadedImage.objects.get(pk=pk),
            expiring_time=expiring_time
        )
        link = reverse_lazy("image-expiring",
                            kwargs={'pk': pk, 'url_str': url_str})
        return Response(link)


class ExpiringImageView(APIView):

    def get(self, request, pk, url_str):
        link = get_object_or_404(ExpiringLink, url_str=url_str)
        if timezone.now() > (
                link.created_at + timedelta(seconds=link.expiring_time)):
            return Response(LINK_EXPIRED)
        return HttpResponse(link.image.image, content_type="image/jpeg")
