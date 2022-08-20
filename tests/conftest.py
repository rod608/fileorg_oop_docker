import os
import pytest

from app.organize.directory_org import OrganizeDirectory
from app.formats import Format
from organize_script import my_formats


# Format Fixtures
@pytest.fixture()
def default_formats_dict() -> dict:
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
def preferred_formats() -> Format:
    """ Dictionary w/ my preferred formats. """
    pref_f = {
        "audio_formats": (".3ga", ".aac", ".ac3", ".aif", ".aiff",
                          ".alac", ".amr", ".ape", ".au", ".dss",
                          ".flac", ".flv", ".m4a", ".m4b", ".m4p",
                          ".mp3", ".mpga", ".ogg", ".oga", ".mogg",
                          ".opus", ".qcp", ".tta", ".voc", ".wav",
                          ".wma", ".wv"),

        "video_formats": (".webm", ".MTS", ".M2TS", ".TS", ".mov",
                          ".mp4", ".m4p", ".m4v", ".mxf"),

        "image_formats": (".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png",
                          ".gif", ".webp", ".svg", ".apng", ".avif"),

        "rom_extensions": (".nes", ".smc", ".sfc", ".gen", ".n64", ".gb", ".gbc",
                           ".gba", ".nds", ".dsi", ".cia", ".3ds", ".gcm", ".nkit.iso",
                           ".iso", ".wbfs", ".nsp", ".xci", ".vpk")

    }
    return pref_f


# DirOrganize Fixtures
@pytest.fixture()
def dir_org(preferred_formats) -> OrganizeDirectory:
    """ DirOrganize Obj w/ Arguments for organizing a desktop. """
    formats = my_formats()  # Custom format obj made above.
    paths = (os.path.expanduser("~/Desktop"), os.path.expanduser("~/Desktop"))  # Desktop Path Twice.
    folders = {}
    return OrganizeDirectory()


@pytest.fixture()
def preferred_formats() -> Format:
    """ Creates a Format class w/ my favorite format types and extensions. """
    my_formats()
