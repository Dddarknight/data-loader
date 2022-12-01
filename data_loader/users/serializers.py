from rest_framework import serializers

from data_loader.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username', 'first_name', 'last_name', 'email', 'subscribe_plan'
        ]
