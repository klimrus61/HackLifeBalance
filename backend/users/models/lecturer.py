from django.db import models
from django.utils.text import gettext_lazy as _


class Lecturer(models.Model):
    user = models.OneToOneField(
        "User",
        verbose_name=_("account lecturer"),
        help_text=_("account for interactions with platform"),
        null=True,
        on_delete=models.SET_NULL,
        related_name="lecturer",
    )
    full_name = models.CharField(
        _("full name"),
        help_text=("full name of lecturer"),
    )
    proffession = models.CharField(
        _("proffession"),
        help_text=("the direction of the profession"),
    )
    descriptions = models.TextField(_("descriptions"), help_text=_("please chose solution status"), null=True)


class LecturerMaterial(models.Model):
    lecturer = models.ForeignKey(
        "Lecturer",
        verbose_name=_("lecturer"),
        help_text=_("please chose which lecturer this matetial"),
        related_name="lecturer_materials",
        on_delete=models.CASCADE,
    )
    title = models.CharField(
        _("title material"),
        help_text=("title materia of lecturer matetial"),
    )
    url = models.URLField(
        _("material link"),
        help_text=_("please provide a material link"),
        null=True,
        blank=True,
    )
