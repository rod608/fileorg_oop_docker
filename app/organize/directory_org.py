import os
import shutil

from pathlib import Path
from app.formats import Format


class OrganizeDirectory:
    """ Class for Organizing Files from one Directory into another Directory or Folders """

    def __init__(self, formats_obj: Format, paths: tuple[str, str], folders: dict[str, str] = None):
        """ Constructor & Instance Attributes: Method Overloading not supported in Python 😞 """
        self._formats = formats_obj  # Format Types & Their Extensions.
        self._og_path = paths[0]  # Directory to Organize.
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
        """ Helper Method: Create folders that associate themselves w/ the formats. """
        os.chdir(self._final_path)

        if self._folders:
            for format_type in self._formats.formats:
                if format_type in self._folders:
                    Path(f"{self._folders[format_type]}").mkdir(exist_ok=True)

    def _rm_empty_folders(self) -> None:
        """ Remove empty folders after organization. """
        os.chdir(self._final_path)

        for item in os.listdir():
            os.chdir(self._final_path)
            folder = Path(item)

            if folder.is_dir():
                os.chdir(folder)
                if not os.listdir():
                    os.chdir(self._final_path)
                    folder.rmdir()

    def _move_files(self, files: list[Path]) -> None:
        """ Move files to the final destination. It may  """
        for file in files:
            for file_type in self._formats.formats:
                # Moving Process.
                if file.suffix in self._formats.formats[file_type]:
                    final_location = self._final_path

                    # No folders specified.
                    if not self._folders:
                        shutil.move(file, final_location)
                        break

                    # File Ext tied to a folder. Move file to folders.
                    elif file_type in self._folders:
                        final_location = final_location.rstrip("/") + f"/{self._folders[file_type]}"
                        shutil.move(file, final_location)
                        break

                    # File Ext not tied to a folder. Move file to final destination.
                    else:
                        shutil.move(file, final_location)
                        break
