import pytest

from main import run
from utils import read_file

INPUT_FILE_NAME: str = "input.txt"


@pytest.fixture
def given_input_file():
    return read_file(INPUT_FILE_NAME)


def test_input_file_ok(given_input_file):
    result = run(given_input_file)

    expected_result = ["GOOD LUCK!"]

    assert result == expected_result


def test_input_file_fails(given_input_file):
    result = run(given_input_file)

    expected_result = ["BAD LUCK!"]

    assert result != expected_result
