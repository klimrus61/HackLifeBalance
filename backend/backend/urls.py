from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from . import views

urlpatterns = [
    path(
        route="",
        view=views.health_check,
        name="health_checker",
    ),
    path("internal-data/", admin.site.urls),
    path("api/v1/", include("api.urls"), name="api"),

    path('api/v1/auth/', include('djoser.urls'), name="base_auth"),
    path('api/v1/auth/', include('djoser.urls.jwt'), name="token"),
    path('api/v1/auth/', include('djoser.social.urls'), name="google_auth"),
    # path("auth/", include("djoser.urls"), name="users"),
    # path("auth/", include("djoser.urls.authtoken"), name="token_auth"),
]

urlpatterns += [
    path("api/v1/schema", SpectacularAPIView.as_view(), name="schema"),
    path("api/v1/schema/swagger-ui/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("api/v1/schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
