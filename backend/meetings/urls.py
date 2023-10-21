from django.urls import path
from django.urls import include, path

from rest_framework import routers

from meetings.views import MeetingViewSet

router = routers.DefaultRouter()
router.register("", MeetingViewSet, "meetings")


urlpatterns = [
    path("", include(router.urls), name="meetings"),
]
