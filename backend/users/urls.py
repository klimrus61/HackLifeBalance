from django.urls import include, path

from rest_framework import routers
from users.views import LecturerViewSet, LecturerMaterialViewSet, UserRoleViewSet

router = routers.DefaultRouter()
router.register("", LecturerViewSet, "lecturer")
router.register("materials", LecturerMaterialViewSet, "lecturer_materials")

router_users = routers.DefaultRouter()
router_users.register("roles", UserRoleViewSet, "roles")

urlpatterns = [
    path("lecturer/", include(router.urls), name="lecturer"),
    path("", include(router_users.urls), name="roles"),
]
