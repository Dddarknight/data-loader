from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from data_loader.users import views


urlpatterns = [
    path(
        'token/', TokenObtainPairView.as_view(), name='token_obtain_pair'
    ),
    path(
        'token/refresh/', TokenRefreshView.as_view(), name='token_refresh'
    ),
    path('sign-up/', views.SignUpView.as_view(), name='sign-up'),
    path('', views.UsersView.as_view(), name='users'),
    path('<int:pk>', views.UserView.as_view(), name='user'),
]
