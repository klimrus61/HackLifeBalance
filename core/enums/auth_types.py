from django.db import models


class AuthTypesEnum(models.TextChoices):
    DEFAULT = "default"
    GOOGLE = "google"
