from typing import List, Tuple

from django.utils.text import gettext_lazy as _


def get_choices_with_lazy_text(choices: List[Tuple[str, str]]) -> List[Tuple[str, str]]:
    """
    the function allows you to assemble a choice set for the Django model,
    with wrapping the second argument in get_text_lazy.

    param: choices - > Example: [(str, str), (str, str)]
    """
    if not choices:
        raise TypeError("function should not accept an empty list of values or an iterator as input")
    result = []
    for choice in choices:
        if not isinstance(choice, tuple) or len(choice) != 2:
            raise ValueError(f"Element of choose must be a tuple with len=2\n" f"for example -> (str1, str2)")
        result.append((choice[0], _(choice[1])))
    return result
