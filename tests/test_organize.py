""" Testing the OrganizeDirectory class and its OrganizeDesktop child class. """
import os
from pathlib import Path
from definitions import Definitions
from app.organize.formats import Format
from app.organize.org_desktop import OrganizeDesktop
from app.organize.org_directory import OrganizeDirectory


def test_file_creation(org_dir) -> None:
    """ Testing the file creation functionality. """
    # change CWD to the desktop
    os.chdir(os.path.expanduser("~/Desktop"))
    assert os.getcwd() == "/Users/rod608/Desktop"

    # create some files
    f1 = Definitions.DESKTOP_PATH + "/img.png"
    open(f1, 'a').close()
    f2 = Definitions.DESKTOP_PATH + "/video.mp4"
    open(f2, 'a').close()
    f3 = Definitions.DESKTOP_PATH + "/audio.mp3"
    open(f3, 'a').close()
    f4 = Definitions.DESKTOP_PATH + "/pokemon.gba"
    open(f4, 'a').close()

    # assert they were created, test the method.
    file_set = {"img.png", "video.mp4", "audio.mp3", "pokemon.gba"}
    file_list: list[Path] = []

    for file in os.listdir():
        if file[0] == ".":
            continue
        if file in file_set:
            file_set.remove(file)
            file_list.append(Path(file))

    assert not file_set
    assert org_dir._files() == file_list


def test_folder_creation(org_dir) -> None:
    """ Testing the folder creation functionality. """
    # change the CWD to the destination path.
    os.chdir(org_dir._final_path)
    assert os.getcwd() == Definitions.DOCUMENTS_PATH
