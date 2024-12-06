import pytest

from main import run_1, run_2
from utils import read_matrix

INPUT_FILE_NAME: str = "input.txt"


@pytest.fixture
def given_input_file():
    return read_matrix(INPUT_FILE_NAME)


def test_run_1_input_file_ok(given_input_file):
    result = run_1(given_input_file)

    expected_result = 5145

    assert len(result) == expected_result


def test_run_2_input_file_ok(given_input_file):
    positions_visited = run_1(given_input_file)
    result = run_2(given_input_file, positions_visited)

    expected_result = 1523

    assert result == expected_result
