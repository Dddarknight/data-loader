from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from data_loader.users.models import User


admin.site.register(User, UserAdmin)
