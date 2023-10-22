from rest_framework.permissions import IsAuthenticated


class Moderator(IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        return (
            obj.moderator == request.user
            or request.user.is_staff
            or request.user.is_admin
            or request.user_is_superuser
        )
