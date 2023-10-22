from django.db import models
from django.utils.text import gettext_lazy as _


class MeetingQuestion(models.Model):
    
    meeting = models.ForeignKey(
        "Meeting",
        verbose_name=_("meeting"),
        help_text=_("please link meeting to question"),
        related_name="meeting_questions",
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        "users.User",
        verbose_name=_("user"),
        help_text=_("author question"),
        related_name="user_questions",
        on_delete=models.CASCADE,
    )
    datetime = models.DateTimeField()
