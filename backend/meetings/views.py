from rest_framework_simplejwt.authentication import JWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import decorators, mixins, viewsets
from rest_framework.response import Response
from meetings.models import Meeting
from meetings.serializers import MeetingModelSerializer



@decorators.authentication_classes([])
@extend_schema_view(list=extend_schema(tags=["meetings"]), retrieve=extend_schema(tags=["meetings"]))
class MeetingViewSet(
    mixins.ListModelMixin, 
    mixins.RetrieveModelMixin, 
    viewsets.GenericViewSet
):
    serializer_class = MeetingModelSerializer
    queryset = Meeting.objects.all()
    filter_backends = (DjangoFilterBackend,)
    