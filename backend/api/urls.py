from django.urls import include, path

urlpatterns = [
    path("meetings/", include("meetings.urls"), name="meetings"),
]
