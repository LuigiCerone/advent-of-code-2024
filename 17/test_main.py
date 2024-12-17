import pytest

from main import run_1
from utils import read_input

INPUT_FILE_NAME: str = "input.txt"


@pytest.fixture
def given_input_file():
    input_registers, program_steps = read_input(INPUT_FILE_NAME)
    return input_registers, program_steps


def test_run_1_input_file_ok(given_input_file):
    output_sequence = run_1(given_input_file[0], given_input_file[1])

    assert output_sequence == "4,3,7,1,5,3,0,5,4"
