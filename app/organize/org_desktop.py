from app.organize.formats import Format
from app.organize.org_directory import OrganizeDirectory
from definitions import Definitions


class OrganizeDesktop(OrganizeDirectory):
    """ Class for Organizing files on the Desktop to the Documents Folder. Files should be moved into folders. """

    def __init__(self, formats_obj: Format, folders: dict[str, str]):
        """ Constructor. Same as OrganizeDirectory's, but with preset paths. """
        old_to_new_path: tuple[str, str] = (Definitions.DESKTOP_PATH, Definitions.DOCUMENTS_PATH)
        super().__init__(formats_obj, old_to_new_path, folders)
