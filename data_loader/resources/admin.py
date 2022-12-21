from django.contrib import admin
from data_loader.resources.models import (
    UploadedImage, ExpiringLink, UploadedFile
)


class UploadedImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'owner', 'created_at')


class ExpiringLinkAdmin(admin.ModelAdmin):
    list_display = ('url_str', 'image', 'created_at', 'expiring_time')


class UploadedFileAdmin(admin.ModelAdmin):
    list_display = ('file', 'owner', 'created_at')


admin.site.register(UploadedImage, UploadedImageAdmin)
admin.site.register(ExpiringLink, ExpiringLinkAdmin)
admin.site.register(UploadedFile, UploadedFileAdmin)
