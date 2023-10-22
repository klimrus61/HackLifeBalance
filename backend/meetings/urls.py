from django.urls import path
from django.urls import include, path

from rest_framework import routers

from meetings.views import MeetingGETViewSet, MeetingCUDViewSet, QuestionViewSet

router = routers.DefaultRouter()
router.register("", MeetingGETViewSet, "meetings")
router.register("", MeetingCUDViewSet, "meetings_CUD")
router.register('questions', QuestionViewSet, "questions")

urlpatterns = [
    path("", include(router.urls), name="meetings"),
]
