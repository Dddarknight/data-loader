from rest_framework import serializers

from data_loader.resources.models import UploadedImage


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedImage
        fields = ('image', )
