import pytest

from main import run, find_all_areas, compute_perimeter, compute_sides
from utils import read_matrix

INPUT_FILE_NAME: str = "input.txt"
EXAMPLE_FILE_NAME: str = "example_1.txt"


@pytest.fixture
def given_input_file():
    return read_matrix(INPUT_FILE_NAME)


@pytest.fixture
def given_example_file():
    return read_matrix(EXAMPLE_FILE_NAME)


def test_find_all_areas_example_file_ok(given_example_file):
    result = find_all_areas(given_example_file)

    assert result == {
        "A": [[(0, 0), (0, 1), (0, 2), (0, 3)]],
        "B": [[(1, 0), (2, 0), (2, 1), (1, 1)]],
        "C": [[(1, 2), (2, 2), (2, 3), (3, 3)]],
        "D": [[(1, 3)]],
        "E": [[(3, 0), (3, 1), (3, 2)]],
    }


def test_compute_perimeter_example_file_ok(given_example_file):
    result = compute_perimeter([(0, 0), (0, 1)])
    assert result == 6


def test_compute_sides_example_file_ok(given_example_file):
    result = compute_sides([(0, 0), (0, 1)])
    assert result == 4


def test_run_1_input_file_ok(given_input_file):
    stones_number = run(given_input_file, part_1=True)

    assert stones_number == 1518548


def test_run_2_input_file_ok(given_input_file):
    stones_number = run(given_input_file, part_1=False)

    assert stones_number == 909564
