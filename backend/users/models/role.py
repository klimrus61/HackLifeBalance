from django.db import models
from django.utils.text import gettext_lazy as _

from core.constants.users import RoleTypes
from core.utils.django_utils import get_choices_with_lazy_text


class UserRole(models.Model):
    user = models.ForeignKey(
        "User",
        verbose_name=_("user"),
        help_text=_("Please specify the user for this role"),
        related_name="roles",
        on_delete=models.CASCADE,
    )
    role = models.CharField(
        _("user role name"),
        help_text=_("Please chose role for this user"),
        choices=get_choices_with_lazy_text(RoleTypes.get_choices()),
    )

    def __str__(self):
        return f"{self.user}-{self.role}"

    class Meta:
        verbose_name = _("User role")
        verbose_name_plural = _("User roles")
        constraints = (
            models.UniqueConstraint(
                fields=("user", "role"),
                name="unique_user_role",
            ),
        )
