from django.urls import path, re_path
from django.conf import settings
from django.views.static import serve

from data_loader.resources import views


urlpatterns = [
    path(
        'images/image-upload',
        views.ImageUploadView.as_view(),
        name="image-upload",
    ),
    path(
        'files/file-upload',
        views.FileUploadView.as_view(),
        name="file-upload",
    ),
    path(
        'images/<int:pk>/thumbnail200',
        views.Thumbnail200View.as_view(),
        name="thumbnail200",
    ),
    path(
        'images/<int:pk>/thumbnail400',
        views.Thumbnail400View.as_view(),
        name="thumbnail400",
    ),
    path(
        'images/<int:pk>/original',
        views.OriginalImageView.as_view(),
        name="original",
    ),
    path(
        'images/<int:pk>/<int:expiring_time>',
        views.ExpiringLinkView.as_view(),
        name="link-expiring",
    ),
    path(
        'images/<int:pk>/<str:url_str>',
        views.ExpiringImageView.as_view(),
        name="image-expiring",
    ),
    path(
        'files/my-files',
        views.FilesInfoView.as_view(),
        name="files-info",
    ),
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    })
]
