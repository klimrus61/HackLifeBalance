"""
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from . import views
from .settings import DEBUG

urlpatterns = [
    path(
        route="",
        view=views.health_check,
        name="health_checker",
    ),
    path("admin/", admin.site.urls),
      path(
        "users/auth/",
        include("apps.users.urls.auth"),
        name="users_auth",
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if DEBUG:
    urlpatterns.extend(
        [
            path("schema/", SpectacularAPIView.as_view(), name="schema"),
            path(
                "docs/",
                SpectacularSwaggerView.as_view(
                    template_name="swagger-ui.html",
                    url_name="schema",
                ),
                name="swagger-ui",
            ),
        ]
    )
pass