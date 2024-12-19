import pytest

from main import run
from utils import read_input

INPUT_FILE_NAME: str = "input.txt"


@pytest.fixture
def given_input_file():
    available_patterns, requested_designs = read_input(INPUT_FILE_NAME)
    return available_patterns, requested_designs


def test_run_1_input_file_ok(given_input_file):
    available_patterns, requested_designs = given_input_file
    num_designs = run(available_patterns, requested_designs, True)

    assert num_designs == 213


def test_run_2_input_file_ok(given_input_file):
    available_patterns, requested_designs = given_input_file
    count_ways = run(available_patterns, requested_designs, False)

    assert count_ways == 1016700771200474
