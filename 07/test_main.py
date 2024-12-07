import pytest

from main import run_1, run_2
from utils import read_input

INPUT_FILE_NAME: str = "input.txt"


@pytest.fixture
def given_input_file():
    results, numbers = read_input(INPUT_FILE_NAME)
    return results, numbers


def test_run_1_input_file_ok(given_input_file):
    result = run_1(given_input_file[0], given_input_file[1])

    expected_result = 932137732557

    assert result == expected_result


def test_run_2_input_file_ok(given_input_file):
    result = run_2(given_input_file[0], given_input_file[1])

    expected_result = 661823605105500

    assert result == expected_result
