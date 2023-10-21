from core.mixins import ChoiceStrMixin

DEFAULT_LESSON_DURATION_MINUTE = 90


class SolutionApprovedTeacherStatuses(ChoiceStrMixin):
    APPROVED = "approved"
    WRONG = "wrong"


class SolutionStudentStatuses(ChoiceStrMixin):
    VIEWED = "viewed"
    DONE = "done"


class SolutionsStatus(ChoiceStrMixin):
    NOT_VIEWED = "not viewed"
    VIEWED = "viewed"
    DONE = "done"
    APPROVED = "approved"
    WRONG = "wrong"


class ScheduleStatus(ChoiceStrMixin):
    CANCELLED = "cancelled"
    PASSED = "already passed"
    NOT_STARTED = "not started"


class GroupType(ChoiceStrMixin):
    ONLINE = "online"
    OFFLINE = "offline"
