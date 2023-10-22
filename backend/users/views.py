from core.permissions.unauthenticated import ReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import OpenApiExample, OpenApiParameter, extend_schema
from rest_framework import decorators, mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from users.models import Lecturer
from users.serializers import LecturerSerializer


class LecturerViewSet(viewsets.ModelViewSet):
    serializer_class = LecturerSerializer
    queryset = Lecturer.objects.all()
    filter_backends = (DjangoFilterBackend,)
    permission_classes = [IsAuthenticated | ReadOnly]
