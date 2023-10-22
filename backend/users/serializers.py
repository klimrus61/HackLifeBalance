from rest_framework import serializers
from users.models import User

from djoser.serializers import UserCreateSerializer as UserCreateSerializer_


class UserSerializer(serializers.ModelSerializer):
    roles = serializers.SlugRelatedField(slug_field="role", many=True, read_only=True)

    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name", "roles")

class UserCreateSerializer(UserCreateSerializer_):
    class Meta:
        model = User
        fields = ("id", "email", "first_name", "last_name", "password")