import logging
from io import BytesIO
from os import PathLike, listdir, makedirs, path
from zipfile import ZipFile
from zipfile import error as ZipError


class ZipService:
    """Service for handling zip files.

    This class provides methods for zipping and unzipping files and directories.

    Args:
        None

    Methods:
        zip(files_directory, destination_file): Compress files from a directory into a zip file.
        unzip(file, destination_dir): Extract the contents of a zip file to a specified directory.
        unzip_from_memory(file, destination_dir): Extract the contents of a zip file from memory to a specified directory.

    Raises:
        None
    """

    def __init__(self) -> None:
        ...

    def __create_dir(self, dir_path) -> None:
        """Create a directory if it does not exist.

        Args:
            dir_path: The path of the directory to be created.

        Returns:
            None

        Raises:
            OSError: If there is an error creating the directory.
        """

        try:
            if not path.exists(dir_path):
                makedirs(path.dirname(dir_path))
        except OSError:
            logging.exception("Error creating directory")

    def zip(self, files_directory: PathLike, destination_file: str | PathLike) -> None:
        """Compress files from a directory into a zip file.

        Args:
            files_directory (PathLike): The directory containing the files to be zipped.
            destination_file (str or PathLike): The path where the zip file will be saved.

        Returns:
            None

        Raises:
            ZipError: If there is an error during the zipping process.
        """

        try:
            files = listdir(files_directory)
            with ZipFile(destination_file, "wb") as f:
                for file in files:
                    f.write(file)
        except ZipError:
            logging.exception("Error zipping data")

    def __unzip(self, file: str, destination_dir: str | PathLike) -> None:
        """Extract the contents of a zip file to a specified directory.

        Args:
            file (str): The path of the zip file to be extracted.
            destination_dir (str or PathLike): The directory where the contents will be extracted.

        Returns:
            None

        Raises:
            ZipError: If there is an error during the extraction process.
        """

        self.__create_dir(destination_dir)
        try:
            with ZipFile(file, "rb") as f:
                f.extractall(path=destination_dir)
        except ZipError:
            logging.exception("Error extracting data from zip file")

    def unzip(self, file: PathLike, destination_dir: str | PathLike) -> None:
        """Extract the contents of a zip file to a specified directory.

        Args:
            file (PathLike): The path of the zip file to be extracted.
            destination_dir (str or PathLike): The directory where the contents will be extracted.

        Returns:
            None

        Raises:
            None
        """

        self.__unzip(file=file, destination_dir=destination_dir)

    def unzip_from_memory(self, file: bytes, destination_dir: str | PathLike) -> None:
        """Extract the contents of a zip file from memory to a specified directory.

        Args:
            file (bytes): The bytes representing the zip file.
            destination_dir (str or PathLike): The directory where the contents will be extracted.

        Returns:
            None

        Raises:
            None
        """

        self.__unzip(file=BytesIO(file), destination_dir=destination_dir)
