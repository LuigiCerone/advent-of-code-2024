import pytest

from main import run_1, run_2
from utils import read_matrix

INPUT_FILE_NAME: str = "input.txt"


@pytest.fixture
def given_input_file():
    return read_matrix(INPUT_FILE_NAME)


def test_run_1_input_file_ok(given_input_file):
    optimal_cost = run_1(
        given_input_file,
    )

    assert optimal_cost == 99448


def test_run_2_input_file_ok(given_input_file):
    tiles = run_2(given_input_file)

    assert tiles == 498
