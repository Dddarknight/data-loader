from django.http import HttpResponse

from data_loader.resources.models import UploadedImage


class ThumbnailMixin:

    def get(self, request, pk):
        thumbnail = UploadedImage.objects.get(pk=pk).make_thumbnail(self.size)
        response = HttpResponse(content_type="image/jpeg")
        thumbnail.save(response, "JPEG")
        return response


class ImageMixin:

    def get(self, request, pk):
        image = UploadedImage.objects.get(pk=pk).image
        return HttpResponse(image, content_type="image/jpeg")
