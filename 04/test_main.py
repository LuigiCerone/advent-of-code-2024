import pytest

from main import run_1, run_2
from utils import read_matrix

INPUT_FILE_NAME: str = "input.txt"


@pytest.fixture
def given_input_file():
    return read_matrix(INPUT_FILE_NAME)


def test_run_1_with_input(given_input_file):
    result = run_1(given_input_file)

    expected_result = 2401

    assert result == expected_result


def test_run_2_with_input(given_input_file):
    result = run_2(given_input_file)

    expected_result = 1822

    assert result == expected_result
