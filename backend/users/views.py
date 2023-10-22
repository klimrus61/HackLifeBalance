from core.permissions.unauthenticated import ReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import OpenApiExample, OpenApiParameter, extend_schema
from users.permissions import Moderator
from rest_framework import decorators, mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from users.models import Lecturer, LecturerMaterial, UserRole
from users.serializers import LecturerSerializer, LecturerMaterialSerializer, UserRoleSerializer


class LecturerViewSet(viewsets.ModelViewSet):
    serializer_class = LecturerSerializer
    queryset = Lecturer.objects.all()
    filter_backends = (DjangoFilterBackend,)
    permission_classes = [IsAuthenticated | ReadOnly]


class LecturerMaterialViewSet(viewsets.ModelViewSet):
    serializer_class = LecturerMaterialSerializer
    queryset = LecturerMaterial.objects.all()
    filter_backends = (DjangoFilterBackend,)
    permission_classes = [Moderator]

class UserRoleViewSet(viewsets.ModelViewSet):
    serializer_class = UserRoleSerializer
    queryset = UserRole.objects.all()
    filter_backends = (DjangoFilterBackend,)
    permission_classes = [Moderator]
