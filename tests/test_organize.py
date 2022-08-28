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


def test_move_files(org_dir) -> None:
    """ Testing the file moving functionality. Very important for organization. """
    # add an extension to org_dir that isn't tied to a folder.
    org_dir._formats.formats["fake_format"].add(".mp5")
    assert ".mp5" in org_dir._formats.formats["fake_format"]

    # change CWD to the desktop, create fake mp5 video file.
    os.chdir(org_dir._og_path)
    assert os.getcwd() == os.path.expanduser("~/Desktop")
    # open(org_dir._og_path + "/fake.mp5", 'a').close()

    # create files for moving.
    ext_set = set()  # will use later to assert file creation.

    for f_type in org_dir._formats.formats:
        file_name = f_type.split("_")[0]  # audio, video, image, rom w/ each of their ext
        for f_ext in org_dir._formats.formats[f_type]:
            # populate the ext_set
            ext_set.add(f_ext)
            # file creation
            cur_file = Definitions.DESKTOP_PATH + "/" + file_name + f_ext
            open(cur_file, 'a').close()

    # assert that the files were created.
    assert ext_set
    file_list = []  # these files will be moved later.

    for item in os.listdir():
        file = Path(item)
        if not file.suffixes:
            continue

        file_list.append(file)

        cur_ext = "".join(file.suffixes)
        if cur_ext in ext_set:
            ext_set.remove(cur_ext)

    assert not ext_set

    # create folders, move the files, delete empty folders
    org_dir._create_folders()
    org_dir._move_files(file_list)

    os.chdir(org_dir._final_path)
    Path("test_dir").mkdir(exist_ok=True)
    org_dir._rm_empty_folders()

    # assert that the folders exist.
    folder_set = set()
    for item in os.listdir():
        folder = Path(item)
        if folder.is_dir():
            folder_set.add(folder.name)

    assert "test_dir" not in folder_set
    assert "audios" in folder_set and "images" in folder_set and "roms" in folder_set and "videos" in folder_set

    # ensure that files were moved part 1. check the og_path.
    os.chdir(org_dir._og_path)
    # open(org_dir._og_path + "/jimmy.mp7", 'a').close()  # this should be within the dir.

    file_set = set(file_list)
    for item in os.listdir():
        file = Path(item)
        if file.is_dir() or not file.suffixes:
            continue
        else:
            assert file.name not in file_set

    # os.remove(org_dir._og_path + "/jimmy.mp5")

    # ensure that files were moved part 2. check the final_path.
    os.chdir(org_dir._final_path)

    assert os.path.exists(f"{org_dir._final_path}/fake.mp5")
    os.remove(f"{org_dir._final_path}/fake.mp5")

    for file_type in org_dir._folders:
        os.chdir(org_dir._final_path + "/" + org_dir._folders[file_type])
        for item in os.listdir():
            file = Path(item)
            if file in file_set:
                os.remove(file)
                file_set.remove(file)

    assert file_set.pop().name == "fake.mp5"
    assert not file_set

    # end, delete all files from created folders.
    org_dir._rm_empty_folders()
