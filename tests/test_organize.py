""" Testing the OrganizeDirectory class and its OrganizeDesktop child class. """
import os
from pathlib import Path
from definitions import Definitions


def test_file_creation(org_dir) -> None:
    """ Testing the file creation functionality. """
    # change CWD to the desktop.
    os.chdir(os.path.expanduser("~/Desktop"))
    assert os.getcwd() == "/Users/rod608/Desktop"

    # create some files.
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

    # delete created files.
    for file in file_list:
        os.remove(file)

def test_folder_functionality(org_dir) -> None:
    """ Testing the folder creation and empty folder removal functionality. """
    # change the CWD to the destination path.
    os.chdir(org_dir._final_path)
    assert os.getcwd() == Definitions.DOCUMENTS_PATH

    # test documents folder creation.
    org_dir._folders["rod_formats"] = "rods"  # this should not be created.
    org_dir._create_folders()

    folder_set = {"audios", "videos", "images", "roms", "rods"}
    for file in os.listdir():
        folder = Path(file)
        if folder.is_dir() and folder.name in folder_set:
            folder_set.remove(folder.name)

    assert len(folder_set) == 1 and "rods" in folder_set

    # test empty folder removal.
    org_dir._rm_empty_folders()
    assert os.getcwd() == org_dir._final_path
    non_existent_folders = ["audios", "videos", "images", "roms"]

    folder_set = set()
    for file in os.listdir():
        folder = Path(file)
        if folder.is_dir():
            folder_set.add(folder.name)

    for item in non_existent_folders:
        assert item not in folder_set
