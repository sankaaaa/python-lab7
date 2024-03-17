import pytest
import os
from app.io.input import read_file_pyt, read_file_pand


@pytest.fixture
def my_testfile():
    test_content = "hello johny depp"
    testfile_path = "testfile.txt"
    with open(testfile_path, "w") as file:
        file.write(test_content)
    yield testfile_path
    os.remove(testfile_path)


def test_unreal_path():
    path_to_file = "lolnofile.txt"

    try:
        read_file_pyt(path_to_file)
    except FileNotFoundError:
        assert True


def test_no_existing_empty_path():
    path_file = ""

    try:
        read_file_pyt(path_file)
    except FileNotFoundError:
        assert True


def text_valid(testfile):
    test_content = "hello johny depp"
    testfile_path = testfile

    text_to_check = read_file_pyt(testfile_path)
    assert text_to_check == test_content


def test_unreal_path_pand():
    path_file = "lolpathnotexist.txt"

    try:
        read_file_pand(path_file)
    except FileNotFoundError:
        assert True


def test_no_existing_path_pand():
    path_file = ""

    try:
        read_file_pand(path_file)
    except FileNotFoundError:
        assert True


def test_valid_pand(my_testfile):
    testfile_path = my_testfile
    real_text = read_file_pand(testfile_path)
    assert not real_text.empty, "DataFrame is empty"
    assert real_text.iloc[0, 0] == "hello johny depp"

