from core.mixins import ChoiceStrMixin


class RoleTypes(ChoiceStrMixin):
    EMPLOYEE = "employee"
    LECTURER = "lecturer"
    MODERATOR = "moderator"

