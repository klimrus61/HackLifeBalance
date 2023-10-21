from core.mixins import ChoiceStrMixin


class ImageTaskType(ChoiceStrMixin):
    SOLUTION_EXAMPLE = "solution_example"
    TRAINING_EXAMPLE = "training_example"
    ILLUSTRATION = "illustration"


class FileTaskType(ChoiceStrMixin):
    VIDEO = "video"
    GIF = "gif"
    MANUAL = "manual"
    FILE = "file"
    CODE_FILE = "code_file"


class TaskType(ChoiceStrMixin):
    CODE = "code"
    CODE_FREE = "code free"
    TEST = "test task"
    QUESTION_TASK = "question task"
