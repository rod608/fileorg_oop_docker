import os
import shutil

from pathlib import Path
from app.organize.formats import Format


class OrganizeDirectory:
    """ Class for Organizing Files in a Directory. Files can be moved to another directory and/or within folders. """

    def __init__(self, formats_obj: Format, paths: tuple[str, str], folders: dict[str, str] = None):
        """ Instance Attributes. Specify format types/extensions, paths to organize, and folders to create. """
        self._formats = formats_obj  # Format Types & Their Extensions.
        self._og_path = paths[0]     # Directory w/ Files to Organize.
        self._final_path = paths[1]  # Target Directory. Folders are created, files are moved.
        self._folders = folders if folders else {}  # format_type -> folder_name

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
        os.chdir(self._og_path)

        files = []
        for item in os.listdir():
            if item[0] == ".":
                continue

            file = Path(item)
            if not file.suffix:
                continue
            else:
                files.append(Path(item))

        return files

    def _create_folders(self) -> None:
        """ For each key in the 'folders' dictionary, create a folder in the final dir if the format type is valid.  """
        os.chdir(self._final_path)

        if self._folders:
            for format_type in self._formats.formats:
                if format_type in self._folders:
                    Path(f"{self._folders[format_type]}").mkdir(exist_ok=True)

    def _rm_empty_folders(self) -> None:
        """ After organization, delete all empty folders. """
        os.chdir(self._final_path)

        for item in os.listdir():
            os.chdir(self._final_path)
            folder = Path(item)

            if folder.is_dir():
                os.chdir(folder)
                if not os.listdir():
                    os.chdir(self._final_path)
                    folder.rmdir()

        os.chdir(self._final_path)

    def _move_files(self, files: list[Path]) -> None:
        """ Move files from og_path to final_path, potentially within folders as well. """
        os.chdir(self._og_path)

        for file in files:
            for file_type in self._formats.formats:
                # Moving Process.
                if file.suffix in self._formats.formats[file_type]:
                    final_location = self._final_path

                    # No folders specified.
                    if not self._folders:
                        # Move if the file doesn't already exist in the final path.
                        if not os.path.exists(final_location + f"/{file.name}"):
                            shutil.move(file, final_location)
                        break

                    # File Ext tied to a folder. Move file to folders.
                    elif file_type in self._folders:
                        final_location = final_location.rstrip("/") + f"/{self._folders[file_type]}"
                        # Move if the file doesn't already exist in the final path.
                        if not os.path.exists(final_location + f"/{file.name}"):
                            shutil.move(file, final_location)
                        break

                    # File Ext not tied to a folder. Move file to final destination.
                    else:
                        # Move if the file doesn't already exist in the final path.
                        if not os.path.exists(final_location + f"/{file.name}"):
                            shutil.move(file, final_location)
                        break
