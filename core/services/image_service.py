import os
from io import BytesIO
from typing import Union

from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image


class ImageFileManager:
    """Utility class for managing image files and generating thumbnails.

    Attributes:
        _allowed_formats (list[str]): List of allowed image formats for generating thumbnails.
    """

    _allowed_formats = [
        "jpeg",
    ]

    def get_file_extension(self, file: InMemoryUploadedFile) -> str:
        """Generate a hashed filename for the given file.

        Args:
            file (Union[InMemoryUploadedFile, BytesIO]): The file object.
            format (str, optional): The file format (e.g., 'jpeg'). Defaults to None.

        Returns:
            str: The hashed filename with the appropriate extension.

        Raises:
            ValueError: If an unsupported format is provided.
        """

        _, ext = os.path.splitext(file.name)
        return ext[1:]

    def get_hashed_filename(
        self,
        file: Union[InMemoryUploadedFile, BytesIO],
        format: str = None,
    ) -> str:
        """Generate a hashed filename for the given file.

        Args:
            file (Union[InMemoryUploadedFile, BytesIO]): The file object.
            format (str, optional): The file format (e.g., 'jpeg'). Defaults to None.

        Returns:
            str: The hashed filename with the appropriate extension.

        Raises:
            ValueError: If an unsupported format is provided.
        """

        hashed_name = str(hash(file))

        if format is None:
            if isinstance(file, BytesIO):
                raise ValueError("Provide explicit file format for BytesIO object")
            format = self.get_file_extension(file=file)

        format = format.lower()

        if format not in self._allowed_formats:
            raise ValueError(f"Unsupported format type: {format.upper()}")

        return f"{hashed_name}.{format}"

    def create_image_thumbnail(self, file: InMemoryUploadedFile):
        """Create a thumbnail image from the given file.

        Args:
            file (InMemoryUploadedFile): The file object.

        Returns:
            InMemoryUploadedFile: The thumbnail image as an InMemoryUploadedFile object.
        """

        format = self.get_file_extension(file=file)

        image = Image.open(file.file)
        image.thumbnail((48, 48), Image.ANTIALIAS)

        thumbnail_bytes = BytesIO()
        image.save(thumbnail_bytes, format=format.upper())

        thumbnail_name = self.get_hashed_filename(file=thumbnail_bytes, format=format)

        thumbnail_file = InMemoryUploadedFile(
            file=thumbnail_bytes,
            field_name=None,
            name=thumbnail_name,
            content_type=f"image/{format}",
            size=len(thumbnail_bytes.getvalue()),
            charset=None,
        )

        return thumbnail_file
