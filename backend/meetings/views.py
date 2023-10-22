from rest_framework_simplejwt.authentication import JWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import decorators, mixins, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from meetings.models import Meeting, MeetingQuestion
from meetings.serializers import MeetingModelSerializer, MeetingQuestionSerializer
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
@extend_schema_view(update=extend_schema(tags=["meetings"]), create=extend_schema(tags=["meetings"]))
class MeetingCUDViewSet(
    mixins.UpdateModelMixin, 
    mixins.CreateModelMixin, 
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = MeetingModelSerializer
    queryset = Meeting.objects.all()
    filter_backends = (DjangoFilterBackend,)

@extend_schema(tags=["questions"])
class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = MeetingQuestionSerializer
    permission_classes = [IsAuthenticated]
    queryset = MeetingQuestion.objects.all()
    filter_backends = (DjangoFilterBackend,)

