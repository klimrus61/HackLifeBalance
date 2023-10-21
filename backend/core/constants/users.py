from core.mixins import ChoiceStrMixin


class RoleTypes(ChoiceStrMixin):
    STUDENT = "student"
    TEACHER = "teacher"
    MODERATOR = "moderator"
    ADMIN = "admin"
    SUPERUSER = "superuser"
