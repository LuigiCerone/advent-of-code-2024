import pytest

from main import NUMBER_BLINKS_PART_1, NUMBER_BLINKS_PART_2, process_stone, run
from utils import read_int_list

INPUT_FILE_NAME: str = "input.txt"
EXAMPLE_FILE_NAME: str = "example_2.txt"


@pytest.fixture
def given_input_file():
    return read_int_list(INPUT_FILE_NAME)


@pytest.fixture
def given_example_file():
    return read_int_list(EXAMPLE_FILE_NAME)


def test_process_stone():
    assert process_stone(0) == [1]

    assert process_stone(1) == [2024]

    assert process_stone(12) == [1, 2]


def test_blink_example_file(given_example_file):
    stones_number = run(given_example_file, 1)

    assert stones_number == 3


def test_run_1_input_file_ok(given_input_file):
    stones_number = run(given_input_file, NUMBER_BLINKS_PART_1)

    assert stones_number == 175006


def test_run_2_input_file_ok(given_input_file):
    stones_number = run(given_input_file, NUMBER_BLINKS_PART_2)

    assert stones_number == 207961583799296
