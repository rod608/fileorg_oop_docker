""" Testing the Format class. """
from app.formats import Format


def test_constructor(f_default, f_full):
    """ Testing using the 'secondary' constructor (with args) """
    assert isinstance(f_default, Format)
    assert isinstance(f_full, Format)

    assert f_default.formats == {}
    assert not f_default.formats
    assert f_full.get_format_types() == ("music", "arcade", "videos")

    assert isinstance(f_full.formats["music"], set)
    assert isinstance(f_full.formats["arcade"], set)
    assert isinstance(f_full.formats["videos"], set)


def test_format_type_methods(f_default, f_full):
    """ Testing the add, get, remove, and clear methods related to Format Types. """
    f_default.add_format_type("music")
    f_default.add_format_type("arcade")
    assert f_default.get_format_types() == ("music", "arcade")
    assert f_full.get_format_types() == ("music", "arcade", "videos")

    f_full.rm_format_type("videos")
    f_default.rm_format_type("arcade")
    assert f_full.get_format_types() == ("music", "arcade")
    assert f_default.get_format_types() == ("music",)

    f_default.rm_format_type("music")
    f_default.rm_format_type("nothing")
    assert f_default.get_format_types() == ()
    assert f_full.get_format_types() == ("music", "arcade")

    f_default.add_format_type("music")
    f_full.clear()
    assert f_default.get_format_types() == ("music",)
    assert f_full.get_format_types() == ()


def test_extension_methods(f_default, f_full):
    """ Testing the add, get, remove, and clear methods related to Format Extensions. """
    # Edge Case: Remove Nothing
    f_default.rm_ext("fake_format", ["fake_ext1", "fake_ext2"])
    assert not f_default.formats
    assert not f_default.get_ext("fake_format")

    # Adding formats to a "music" format type.
    f_default.add_format_type("music")
    f_default.add_ext("music", ["mp3", "flac"])
    assert ".mp3" in f_default.formats["music"] and ".flac" in f_default.formats["music"]
    assert not f_full.formats["music"]

    # Copying the "music" extensions to a "production" format type.
    f_default.add_format_type("music3")
    f_default.copy_ext("music", "music2")
    assert f_default.formats["music"] == f_default.formats["music2"]
    assert ".mp3" in f_default.formats["music2"] and ".flac" in f_default.formats["music2"]
    assert not f_default.formats["music3"]

    # Deleting the "music" format type's extensions.
    f_default.rm_ext("music", ["mp3"])
    f_default.rm_ext("music", ["mp3"])
    assert ".mp3" not in f_default.formats["music"] and ".flac" in f_default.formats["music"]
    f_default.rm_ext("music", ["flac"])
    assert not f_default.formats["music"]
