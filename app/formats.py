import collections
from typing import Sequence


class Format:
    """ A class that defines the formats users have stored and their operations. Used in the Organize Class. """

    def __init__(self, f_types=None):
        """ Constructor & Instance Attributes. Sets up the self._formats dict w/ format types and their extensions. """
        self._formats: dict[str, set[str]] = collections.defaultdict(set)  # format_type -> extensions

        # Add each format type as a key in self._formats.
        if f_types:
            for f_type in f_types:
                self._formats[f_type] = set()

    # Format_Type Methods
    def add_format_type(self, new_type: str) -> None:
        """ Add format types, with or without extensions. """
        if new_type not in self._formats:
            self._formats[new_type] = set()

    def rm_format_type(self, format_type: str) -> None:
        """ Delete an existing format type. """
        if format_type in self._formats:
            del self._formats[format_type]

    def get_format_types(self) -> tuple:
        """ Return the format types as a tuple. """
        return tuple(self._formats.keys())

    def clear(self) -> None:
        """ Clears the instance attribute entirely. """
        self._formats.clear()

    # Format_Extensions Methods
    def add_ext(self, f_type: str, f_ext: list[str]) -> None:
        """ Add Extensions to already existing types. """
        if f_type in self._formats:
            # Organize the extensions w/ a helper method.
            organized_exts = Format._organize_ext(f_ext)
            for ext in organized_exts:
                self._formats[f_type].add(ext)

    def get_ext(self, f_type: str) -> Sequence[str]:
        """ Return the extensions of a specific format """
        if f_type in self._formats:
            return tuple(self._formats[f_type])
        # Edge Case: f_type not a key in the dict
        return tuple()

    def rm_ext(self, f_type, f_ext: list[str]):
        """ Remove Extensions from already existing types. """
        # If the format type exists within self.formats...
        if f_type in self._formats:
            # Prepare the f_ext list.
            organized_extensions = self._organize_ext(f_ext)
            # Then, check for each occurrence of each ext and remove it.
            for ext in organized_extensions:
                if ext in self._formats[f_type]:
                    self._formats[f_type].remove(ext)

    def copy_ext(self, og_type, new_type):
        """ Copy Extensions from one format type to another, existing or not. """
        # If the original format type exists within self.formats...
        if og_type in self._formats:
            # No matter what, get a copy of og_type's elements
            old_extensions: set[str] = self._formats[og_type].copy()
            # Check to see if new_type exists as well.
            if new_type in self._formats:
                # If it does, add og_type's extensions to new_type's existing ones.
                for ext in old_extensions:
                    self._formats[new_type].add(ext)
            # Otherwise, create a new_type with og_type's extensions.
            else:
                self._formats[new_type] = old_extensions

    # Private Methods: Abstraction (limiting access to implementation)
    @staticmethod
    def _organize_ext(f_ext: list[str]) -> list[str]:
        """ Extension Formatter Method: Returns a copy of the ext list w/ removed duplicates and proper formatting. """
        new_ext_lst = f_ext.copy()
        new_ext_lst = Format._rm_duplicate_ext(new_ext_lst)
        Format._check_extensions(new_ext_lst)
        return new_ext_lst

    @staticmethod
    def _rm_duplicate_ext(f_ext: list[str]) -> list[str]:
        """ Extension Helper Method: Remove duplicate extensions. """
        res = set(f_ext)
        return list(res)

    @staticmethod
    def _check_extensions(f_ext: list[str]) -> None:
        """ Extension Helper Method: Ensures extensions begin w/ a period. """
        for i in range(len(f_ext)):
            if f_ext[i][0] != ".":
                f_ext[i] = f".{f_ext[i]}"

    # Overriding built-in Dunder Methods & Operator Overloading
    def __str__(self) -> str:
        """ toString Method """
        return str(self._formats)

    def __eq__(self, other) -> bool:
        if self._formats == other.formats:
            return True
        return False

    # Getters & Setters: The Python Way
    @property
    def formats(self) -> dict[str, set[str]]:
        """ Getter Method for self._formats """
        return self._formats

    @formats.setter
    def formats(self, new_formats: dict[str, set[str]]) -> None:
        """ Setter Method for self._formats """
        self._formats = new_formats
