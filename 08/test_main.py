import pytest

from main import compute_antennas, run_1, run_2
from utils import read_matrix

INPUT_FILE_NAME: str = "input.txt"


@pytest.fixture
def given_input_file():
    return read_matrix(INPUT_FILE_NAME)


def test_run_1_input_file_ok(given_input_file):
    antennas = compute_antennas(given_input_file)

    result = run_1(antennas, given_input_file)

    expected_result = 423

    assert result == expected_result


def test_run_2_input_file_ok(given_input_file):
    result = run_2(given_input_file[0], given_input_file[1])

    expected_result = 661823605105500

    assert result == expected_result
