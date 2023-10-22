from django.urls import include, path

from rest_framework import routers
from users.views import LecturerViewSet

router = routers.DefaultRouter()
router.register("", LecturerViewSet, "lecturer")

urlpatterns = [
    path("", include(router.urls), name="lecturer"),
]
