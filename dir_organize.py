import os
import shutil

from pathlib import Path
from formats import Format


class DirOrganize:
    """ Class for Organizing Files from one Directory into another Directory or Folders """

    def __init__(self, formats_obj: Format, paths: tuple[str, str], folders: dict[str, str] = {}):
        """ Constructor & Instance Attributes: Overloading not supported in Python 😞 """
        self._formats = formats_obj  # Format Types & Their Extensions.
        self._folders = folders      # format_type -> folder_name
        self._og_path = paths[0]     # Directory to Organize
        self._final_path = paths[1]  # Target Directory: Folders are created, files are moved.

    def organize(self) -> None:
        """ Organize Method: Move all files w/ certain extensions into their specified folders. """
        # Step 1: Create folders if needed.
        os.chdir(self._final_path)
        self._create_folders()

        # Step 2: Ready the files for moving.
        files: list[Path] = self._files()

        # Edge case: No files to organize.
        if not files:
            return

        # Step 3: Organize Files.
        for file in files:
            for file_type in self._formats.formats:
                # Moving Process.
                if file.suffix in self._formats.formats[file_type]:
                    final_location = self._final_path
                    # No folders specified.
                    if not self._folders:
                        shutil.move(file, final_location)
                        continue
                    # Folders specified.
                    elif file_type in self._folders:
                        final_location = final_location.rstrip("/") + f"/{self._folders[file_type]}"
                        shutil.move(file, final_location)
                        continue

        # Step 4: Delete Empty Folders.
        self._rm_empty_folders()

    def _create_folders(self) -> None:
        """ Helper Method: Create folders that associate themselves w/ the formats. """
        if self._folders:
            for format_type in self._formats.formats:
                if format_type in self._folders:
                    Path(f"{self._folders[format_type]}").mkdir(exist_ok=True)

    def _files(self) -> list[Path]:
        """ Return a list of Path objects instantiated w/ all the files in the directory in mind. """
        os.chdir(self._og_path)

        files = []
        for item in os.listdir():
            if item[0] == ".":
                continue
            else:
                file = Path(item)
                if not file.suffix:
                    continue
                else:
                    files.append(Path(item))

        return files

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
