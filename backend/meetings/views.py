from rest_framework_simplejwt.authentication import JWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import decorators, mixins, viewsets
from rest_framework.response import Response
from meetings.models import Meeting
from meetings.serializers import MeetingModelSerializer
from users.permissions import Moderator



@decorators.authentication_classes([])
@decorators.permission_classes([])
@extend_schema_view(list=extend_schema(tags=["meetings"]), retrieve=extend_schema(tags=["meetings"]))
class MeetingGETViewSet(
    mixins.ListModelMixin, 
    mixins.RetrieveModelMixin, 
    viewsets.GenericViewSet
):
    serializer_class = MeetingModelSerializer
    queryset = Meeting.objects.all()
    filter_backends = (DjangoFilterBackend,)

@decorators.permission_classes([Moderator])
@extend_schema_view(list=extend_schema(tags=["meetings"]), retrieve=extend_schema(tags=["meetings"]))
class MeetingCUDViewSet(
    mixins.UpdateModelMixin, 
    mixins.CreateModelMixin, 
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = MeetingModelSerializer
    queryset = Meeting.objects.all()
    filter_backends = (DjangoFilterBackend,)
