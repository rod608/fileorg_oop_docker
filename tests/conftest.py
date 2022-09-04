import os
import pytest
import logging

from app.organize.formats import Format
from app.organize.org_directory import OrganizeDirectory


# Format Fixtures
@pytest.fixture()
def default_formats_dict() -> dict:
    """ Returns a dictionary w/ audio, video, and image formats paired to a list of their associated extensions. """
    default_formats: dict[str, list[str]] = {
        "audio_formats": [".3ga", ".aac", ".ac3", ".aif", ".aiff",
                          ".alac", ".amr", ".ape", ".au", ".dss",
                          ".flac", ".flv", ".m4a", ".m4b", ".m4p",
                          ".mp3", ".mpga", ".ogg", ".oga", ".mogg",
                          ".opus", ".qcp", ".tta", ".voc", ".wav",
                          ".wma", ".wv"],
        "video_formats": [".webm", ".MTS", ".M2TS", ".TS", ".mov",
                          ".mp4", ".m4p", ".m4v", ".mxf"],
        "image_formats": [".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png",
                          ".gif", ".webp", ".svg", ".apng", ".avif"]
    }
    return default_formats


@pytest.fixture()
def f_default() -> Format:
    """ Format Obj w/ no Arguments. """
    return Format()


@pytest.fixture()
def f_full() -> Format:
    """ Format Obj w/ Format Types """
    return Format(["music", "arcade", "videos"])


@pytest.fixture()
def f_obj_types() -> Format:
    """ Format Obj w/ a format_types Argument. """
    return Format(["music", "arcade", "videos"])


@pytest.fixture()
def f_obj_types_ext(default_formats_dict) -> Format:
    """ Format Obj w/ All Arguments. """
    return Format(f_types_ext=default_formats_dict)


@pytest.fixture()
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


# DirOrganize Fixtures
@pytest.fixture()
def org_dir(my_formats) -> OrganizeDirectory:
    """ DirOrganize Obj w/ Arguments for organizing a desktop. """
    paths = (os.path.expanduser("~/Desktop"), os.path.expanduser("~/Documents"))  # Desktop Path Twice.

    folders = {}
    for f_type in my_formats.formats:
        folders[f_type] = f_type.split("_")[0] + "s"

    return OrganizeDirectory(my_formats, paths, folders)


@pytest.fixture()
def org_desk(my_formats) -> OrganizeDirectory:
    """ DirOrganize Obj w/ Arguments for organizing a desktop. """
    paths = (os.path.expanduser("~/Desktop"), os.path.expanduser("~/Desktop"))  # Desktop Path Twice.

    folders = {}
    for f_type in my_formats.formats:
        folders[f_type] = f_type.split("_")[0] + "s"

    return OrganizeDirectory(my_formats, paths, folders)
