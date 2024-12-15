import pytest

from main import N_COLS, N_ROWS, PART_1_SECONDS, run_1, run_2
from utils import read_input

INPUT_FILE_NAME: str = "input.txt"


@pytest.fixture
def given_input_file():
    return read_input(INPUT_FILE_NAME)


def test_run_1_input_file_ok(given_input_file):
    safety_factor = run_1(given_input_file, PART_1_SECONDS, N_ROWS, N_COLS)

    assert safety_factor == 231852216


def test_run_2_input_file_ok(given_input_file):
    seconds_required = run_2(given_input_file, N_ROWS, N_COLS)

    assert seconds_required == 8158
