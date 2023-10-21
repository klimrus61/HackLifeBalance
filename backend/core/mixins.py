from enum import StrEnum


class ChoiceStrMixin(StrEnum):
    """Mixin for adapting the enum class to the Django choose class"""

    @classmethod
    def get_choices(cls):
        return [(el.value, el.value) for el in cls]
