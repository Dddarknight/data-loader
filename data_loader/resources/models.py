from django.db import models
from django.utils import timezone
from PIL import Image

from data_loader.users.models import User


class UploadedImage(models.Model):

    image = models.ImageField(upload_to='images')
    owner = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'image'
        verbose_name_plural = 'images'

        ordering = ['created_at']

    def make_thumbnail(self, size):
        image_data = Image.open(self.image)
        image_data.thumbnail(size, Image.ANTIALIAS)
        return image_data


class ExpiringLink(models.Model):

    url_str = models.CharField(max_length=100)
    image = models.ForeignKey(UploadedImage, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    expiring_time = models.IntegerField()

    class Meta:
        verbose_name = 'expiring_link'
        verbose_name_plural = 'expiring_links'

        ordering = ['created_at']


class UploadedFile(models.Model):

    file = models.FileField(upload_to='files')
    owner = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'file'
        verbose_name_plural = 'files'

        ordering = ['created_at']
