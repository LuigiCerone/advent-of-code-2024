import pytest

from main import SIMULATE_BYTES, get_corrupted_bytes, run_1
from utils import read_input

INPUT_FILE_NAME: str = "input.txt"


@pytest.fixture
def given_input_file():
    return read_input(INPUT_FILE_NAME)


def test_run_1_input_file_ok(given_input_file):
    corrupted_bytes = get_corrupted_bytes(given_input_file, cut_size=SIMULATE_BYTES)
    num_steps = run_1(corrupted_bytes)

    assert num_steps == 370
