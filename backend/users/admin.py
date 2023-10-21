from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from users.admin_inlines import RoleInline
from users.models import User, UserRole


@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    ...


@admin.register(User)
class UserAdmin(UserAdmin):
    ...