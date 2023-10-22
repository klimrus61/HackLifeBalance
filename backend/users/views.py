from rest_framework import decorators, mixins, viewsets
from core.permissions.unauthenticated import ReadOnly
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from django_filters.rest_framework import DjangoFilterBackend
from users.serializers import LecturerSerializer
from users.models import Lecturer


class LecturerViewSet(viewsets.ModelViewSet):
    serializer_class = LecturerSerializer
    queryset = Lecturer.objects.all()
    filter_backends = (DjangoFilterBackend,)
    permission_classes = [IsAuthenticated|ReadOnly]
