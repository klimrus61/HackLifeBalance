from django.contrib.auth import models as auth_models
from django.contrib.auth import validators
from django.db import models

from ..services import UserManagerService




class UserModel(auth_models.AbstractBaseUser, auth_models.PermissionsMixin, models.Model):
    username_validator = validators.UnicodeUsernameValidator()
    username = models.CharField(
        "username",
        max_length=30,
        unique=True,
        help_text="Required. 20 characters or fewer. Letters, digits and @/./+/-/_ only.",
        validators=[username_validator],
        error_messages={
            "unique": "A user with that username already exists.",
        },
    )
    email = models.EmailField(
        max_length=50,
        unique=True,
        error_messages={
            "unique": "A user with that email already exists.",
        },
    )
    auth_type_id = models.ForeignKey(
        "users.UserAuthTypeModel",
        on_delete=models.CASCADE,
        db_column="auth_type_id",
        related_name="auth_type_for_users",
        null=True,
        blank=True,
    )

    @property
    def is_staff(self):
        return self.is_superuser

    objects = UserManagerService()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    @classmethod
    def normalize_email(cls, email: str) -> str:
        """Normalize given email by making domain part lowercase. If the email given is invalid, it will be returned as
        is.

        Args:
            email (str): Email to be normalized

        Returns:
            str: Normalized email
        """

        try:
            email_name, domain_part = email.strip().rsplit("@", 1)
        except ValueError:
            pass
        else:
            email = email_name + "@" + domain_part.lower()
        return email

    # def check_profile(self, raise_exception: bool = False) -> bool:
    #     exists: bool = UserProfileModel.objects.filter(
    #         user__id=self.id, raise_exception=False
    #     ).exists()
    #     if not exists and raise_exception:
    #         raise DoesNotExistException("Profile does not exist.")
    #     return exists

    # def get_full_name(self) -> str:
    #     profile = UserProfileModel.objects.get(user__id=self.id)
    #     return f"{profile.first_name} {profile.last_name}"

    # @classmethod
    # def update_instance_by_field(cls, attr: str, value: str, update_data: dict) -> "UserModel":
    #     try:
    #         user = cls.objects.get(**{attr: value})
    #     except FieldError:
    #         raise FieldDoesNotExistException(
    #             f"The field '{attr}' does not exist in the '{cls.__name__}'."
    #         )

    #     for instance_attr in update_data.keys():
    #         try:
    #             cls._meta.get_field(instance_attr)
    #             setattr(user, instance_attr, update_data[instance_attr])
    #         except FieldDoesNotExist:
    #             raise FieldDoesNotExistException(
    #                 f"The field '{instance_attr}' does not exist in the '{cls.__name__}'."
    #             )
    #     new_username = update_data.get("username", None)
    #     if new_username is not None:
    #         if cls.objects.filter(username=new_username).exclude(pk=user.pk).exists():
    #             raise BadRequestException(f"Username '{new_username}' already exist")

    #     user.clean_fields()
    #     user.save()
    #     return user

    class Meta:
        db_table = "users"
