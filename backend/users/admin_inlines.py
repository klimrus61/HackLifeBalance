from django.contrib import admin

from users.models import UserRole


class RoleInline(admin.StackedInline):
    extra = 1
    model = UserRole
