from rest_framework import serializers

from data_loader.resources.models import UploadedImage, UploadedFile


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = UploadedImage
        fields = ('image', )


class FileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UploadedFile
        fields = ('file', )
