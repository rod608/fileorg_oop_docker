import os

from dir_organize import DirOrganize
from formats import Format


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


def organize_desktop() -> None:
    """ Organizes my desktop based on my custom Format and DirOrganize classes. """
    formats = my_formats()  # Custom format obj made above.
    paths = (os.path.expanduser("~/Desktop"), os.path.expanduser("~/Desktop"))  # Desktop Path Twice.
    folders = {}

    for format_type in formats.formats:
        folders[format_type] = format_type.split("_")[0] + "s"

    desktop_org = DirOrganize(formats, paths, folders)
    desktop_org.organize()


# main method; signifies a script
if __name__ == "__main__":
    organize_desktop()
