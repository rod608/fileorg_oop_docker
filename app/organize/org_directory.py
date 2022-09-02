import os
import shutil
import logging
import logging.config

from pathlib import Path
from app.organize.formats import Format
from logging_config import LOGGING_CONFIG_DICT


class OrganizeDirectory:
    """ Class for Organizing Files in a Directory. Files can be moved to another directory and/or within folders. """

    def __init__(self, formats_obj: Format, paths: tuple[str, str], folders: dict[str, str] = None):
        """ Instance Attributes. Specify format types/extensions, paths to organize, and folders to create. """
        self._formats = formats_obj  # Format Types & Their Extensions.
        self._og_path = paths[0]     # Directory w/ Files to Organize.
        self._final_path = paths[1]  # Target Directory. Folders are created, files are moved.
        self._folders = folders if folders else {}  # format_type -> folder_name

        # Logging config!
        logging.config.dictConfig(LOGGING_CONFIG_DICT)

    def organize(self) -> None:
        """ Organize Method: Move all files w/ certain extensions into their specified folders. """
        # Step 1: Ready the files for moving.
        files: list[Path] = self._files()

        # Edge Case: No files to organize.
        if not files:
            return

        # Step 2: Create folders if needed.
        self._create_folders()

        # Step 3: Move Files.
        self._move_files(files)

        # Step 4: Delete Empty Folders.
        self._rm_empty_folders()

    def _files(self) -> list[Path]:
        """ Return a list of Path objects that are instantiated w/ the files in the original directory in mind. """
        logger = logging.getLogger("org_logger")
        logger.info(f"self._files(): Searching the og_location \"{self._og_path}\" for files...")

        os.chdir(self._og_path)

        files = []
        for item in os.listdir():
            logger.info(f"cur_item = {item}")
            if item[0] == ".":
                continue

            file = Path(item)
            if not file.suffix:
                continue
            else:
                logger.info(f"Adding {file.name} to file_list.")
                files.append(Path(item))

        logger.info(f"file_list == {files}")
        return files

    def _create_folders(self) -> None:
        """ For each key in the 'folders' dictionary, create a folder in the final dir if the format type is valid.  """
        logger = logging.getLogger("org_logger")
        logger.info(f"self._create_folders(): Creating folders in the final_path \"{self._final_path}\"")

        os.chdir(self._final_path)

        if self._folders:
            for format_type in self._formats.formats:
                if format_type in self._folders:
                    logger.info(f"Creating folder: {self._folders[format_type]}")
                    Path(f"{self._folders[format_type]}").mkdir(exist_ok=True)
                    logger.info(f"folder created or already exists.")


    def _rm_empty_folders(self) -> None:
        """ After organization, delete all empty folders. """
        logger = logging.getLogger("org_logger")
        logger.info(f"self._rm_empty_folders(): Removing empty folders in the final_path \"{self._final_path}\"")

        os.chdir(self._final_path)

        for item in os.listdir():
            os.chdir(self._final_path)
            folder = Path(item)

            if folder.is_dir():
                logger.info(f"cur_folder = {folder.name}")
                os.chdir(folder)

                if not os.listdir():
                    logger.info(f"Preparing to remove empty folder {folder.name}")
                    os.chdir(self._final_path)
                    folder.rmdir()
                    logger.info(f"{folder.name} folder removed.")

        logger.info(f"removal(s) complete. changing CWD to \"{self._final_path}\"")
        os.chdir(self._final_path)

    def _move_files(self, files: list[Path]) -> None:
        """ Move files from og_path to final_path, potentially within folders as well. """
        logger = logging.getLogger("org_logger")
        logger.info(f"self._move_files(): Preparing to move files from the \"{self._og_path}\"")

        os.chdir(self._og_path)

        for file in files:
            for file_type in self._formats.formats:
                # Moving Process.
                if file.suffix in self._formats.formats[file_type]:
                    logger.info(f"Preparing to move file {file.name}")
                    final_location = self._final_path

                    # No folders specified.
                    if not self._folders:
                        # Move if the file doesn't already exist in the final path.
                        self.__move_helper(final_location, file)
                        break

                    # File Ext tied to a folder. Move file to folders.
                    elif file_type in self._folders:
                        final_location = os.path.join(final_location, self._folders[file_type])
                        # Move if the file doesn't already exist in the final path.
                        self.__move_helper(final_location, file)
                        break

                    # File Ext not tied to a folder. Move file to final destination.
                    else:
                        # Move if the file doesn't already exist in the final path.
                        self.__move_helper(final_location, file)
                        break

    @staticmethod
    def __move_helper(final_location, file) -> None:
        """ Helper function for move_files(). Given a file, move if only one of it exists otherwise delete it. """
        logger = logging.getLogger("org_logger")

        if not os.path.exists(os.path.join(final_location, file.name)):
            logger.info(f"Moving to \"{final_location}\"")
            shutil.move(file, final_location)
            logger.info(f"File moved.")
        else:
            logger.info(f"Duplicate File {file.name} found. Removing newest entry.")
            os.remove(file)
            logger.info(f"File removed.")
