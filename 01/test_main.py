import pytest

from main import run_1, run_2
from utils import read_arrays

INPUT_FILE_NAME: str = "input.txt"


@pytest.fixture
def given_input_file():
    return read_arrays(INPUT_FILE_NAME)


def test_input_file_ok_1(given_input_file):
    result = run_1(given_input_file[0], given_input_file[1])

    expected_result = 3574690

    assert result == expected_result


def test_input_file_ok_2(given_input_file):
    result = run_2(given_input_file[0], given_input_file[1])

    expected_result = 22565391

    assert result == expected_result