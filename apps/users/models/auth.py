from django.db import models
from core.enums import AuthTypesEnum


class UserAuthTypeModel(models.Model):
    name = models.CharField(max_length=25, choices=AuthTypesEnum.choices)

    class Meta:
        db_table = "user_auth_type"
