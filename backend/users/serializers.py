from djoser.serializers import UserCreateSerializer as UserCreateSerializer_
from rest_framework import serializers
from users.models import Lecturer, LecturerMaterial, User


class UserSerializer(serializers.ModelSerializer):
    roles = serializers.SlugRelatedField(slug_field="role", many=True, read_only=True)

    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "roles")


class UserCreateSerializer(UserCreateSerializer_):
    class Meta:
        model = User
        fields = ("id", "email", "first_name", "last_name", "password")


class LecturerMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = LecturerMaterial
        fields = "__all__"


class LecturerSerializer(serializers.ModelSerializer):
    lecturer_materials = LecturerMaterialSerializer(many=True)

    class Meta:
        model = Lecturer
        fields = "__all__"
