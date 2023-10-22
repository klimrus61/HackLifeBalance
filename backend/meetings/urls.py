from django.urls import include, path

from meetings.views import MeetingCUDViewSet, MeetingGETViewSet, QuestionViewSet, MeetingOfferViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register("", MeetingGETViewSet, "meetings")
router.register("", MeetingCUDViewSet, "meetings_CUD")
router.register("questions", QuestionViewSet, "questions")
router.register("offer", MeetingOfferViewSet, "offer")

urlpatterns = [
    path("", include(router.urls), name="meetings"),
]
