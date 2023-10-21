from django.db import models
from django.utils.text import gettext_lazy as _

from core.constants.meetings import GroupType
from core.utils.django_utils import get_choices_with_lazy_text


class Meeting(models.Model):
    title = models.CharField(
        _("meeting title"),
        help_text=_("please specify the title of the meeting"),
        max_length=255,
    )
    meeting_theme = models.ForeignKey(
        "MeetingType",
        verbose_name=_("lecturer"),
        help_text=_("please chose lecturer for this group"),
        related_name="lecturer_meetings",
        null=True,
        on_delete=models.SET_NULL,
    )
    meeting_link = models.URLField(
        _("meeting link"),
        help_text=_("please provide a meeting link"),
        null=True,
        blank=True,
    )
    is_active = models.BooleanField(
        _("group is active"),
        help_text=_("check the box if the meeting is active"),
        default=True,
    )
    description = models.TextField(
        _("group description"),
        help_text=_("please enter a description of the meeting"),
        null=True,
        blank=True,
    )
    lecturer = models.ForeignKey(
        "users.User",
        verbose_name=_("lecturer"),
        help_text=_("please chose lecturer for this group"),
        related_name="lecturer_meetings",
        null=True,
        on_delete=models.SET_NULL,
    )

    class Meta:
        verbose_name = _("Meeting")
        verbose_name_plural = _("Meeting")

class MeetingType(models.Model):
    title = models.CharField(
        _("meeting title"),
        help_text=_("please specify the title of the meeting"),
        max_length=255,
    )
    class Meta:
        verbose_name = _("Meeting type")
        verbose_name_plural = _("Meeting types")
