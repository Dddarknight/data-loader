from django.urls import path, re_path
from django.conf import settings
from django.views.static import serve

from data_loader.resources import views


urlpatterns = [
    path('image-upload', views.ImageUploadView.as_view(), name="image-upload"),
    path(
        'thumbnail200/<int:pk>',
        views.Thumbnail200View.as_view(),
        name="thumbnail200",
    ),
    path(
        'thumbnail400/<int:pk>',
        views.Thumbnail400View.as_view(),
        name="thumbnail400",
    ),
    path(
        'original/<int:pk>',
        views.OriginalImageView.as_view(),
        name="original",
    ),
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    })
]
