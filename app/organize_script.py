from app.organize.formats import Format
from organize.org_directory import OrganizeDirectory
from organize.org_desktop import OrganizeDesktop
from definitions import Definitions


def my_formats() -> Format:
    """ Creates a Format class w/ my favorite format types and extensions. """
    f_types = ["audio_formats", "video_formats", "image_formats", "rom_extensions"]
    f = Format(f_types)

    f.add_ext("audio_formats", [".3ga", ".aac", ".ac3", ".aif", ".aiff",
                                ".alac", ".amr", ".ape", ".au", ".dss",
                                ".flac", ".flv", ".m4a", ".m4b", ".m4p",
                                ".mp3", ".mpga", ".ogg", ".oga", ".mogg",
                                ".opus", ".qcp", ".tta", ".voc", ".wav",
                                ".wma", ".wv"])

    f.add_ext("video_formats", [".webm", ".MTS", ".M2TS", ".TS", ".mov",
                                ".mp4", ".m4p", ".m4v", ".mxf"])

    f.add_ext("image_formats", [".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png",
                                ".gif", ".webp", ".svg", ".apng", ".avif"])

    f.add_ext("rom_extensions", [".nes", ".smc", ".sfc", ".gen", ".n64", ".gb", ".gbc",
                                 ".gba", ".nds", ".dsi", ".cia", ".3ds", ".gcm", ".nkit.iso",
                                 ".iso", ".wbfs", ".nsp", ".xci", ".vpk"])

    return f


def organize_desktop_to_documents() -> None:
    """ Organizes the desktop based on the custom Format and DirOrganize classes. """
    formats = my_formats()  # Custom format obj made above.
    paths = (Definitions.DESKTOP_PATH, Definitions.DOCUMENTS_PATH)  # Desktop Path Twice.
    folders = {}

    for format_type in formats.formats:
        folders[format_type] = format_type.split("_")[0] + "s"

    desktop_documents_org = OrganizeDirectory(formats, paths, folders)
    desktop_documents_org.organize()


def organize_desktop_to_folders() -> None:
    """ Organizes the files on the desktop into folders. """
    formats = my_formats()  # Custom format obj made above.
    folders = {}

    for format_type in formats.formats:
        folders[format_type] = format_type.split("_")[0] + "s"

    desktop_org_obj = OrganizeDesktop(formats, folders)
    desktop_org_obj.organize()


# main method; signifies a script
if __name__ == "__main__":
    # setup logs

    # run the script
    # organize_desktop_to_documents()
    organize_desktop_to_folders()
