from django.db import models
from PIL import Image

from data_loader.users.models import User


class UploadedImage(models.Model):

    image = models.ImageField(upload_to='images')
    owner = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def make_thumbnail(self, size):
        image_data = Image.open(self.image)
        image_data.thumbnail(size, Image.ANTIALIAS)
        return image_data
