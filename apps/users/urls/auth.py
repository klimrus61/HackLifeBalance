from django.urls import path

from ..views import (
    google_auth,
    logout,
    refresh_token,
)

urlpatterns = [
    path(
        route="google/",
        view=google_auth,
        name="google_auth",
    ),

    path(
        route="token/refresh/",
        view=refresh_token,
        name="token_refresh",
    ),
    path(
        route="logout/",
        view=logout,
        name="logout",
    ),
]
