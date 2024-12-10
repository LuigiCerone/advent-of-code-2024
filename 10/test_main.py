import pytest

from main import find_starting_points, run
from utils import read_matrix

INPUT_FILE_NAME: str = "input.txt"
EXAMPLE_FILE_NAME: str = "example.txt"


@pytest.fixture
def given_input_file():
    return read_matrix(INPUT_FILE_NAME)


@pytest.fixture
def given_example_file():
    return read_matrix(EXAMPLE_FILE_NAME)


def test_expand_disk_map_example_file(given_example_file):
    result = find_starting_points(given_example_file)

    expected_result = [(0, 0)]

    assert result == expected_result


def test_run_1_input_file_ok(given_input_file):
    score = run(given_input_file, True)

    assert score == 674


def test_run_2_input_file_ok(given_input_file):
    score = run(given_input_file, False)

    assert score == 1372
