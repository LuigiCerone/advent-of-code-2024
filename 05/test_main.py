import pytest

from main import run_1, run_2
from utils import read_file

INPUT_FILE_NAME: str = "input.txt"


@pytest.fixture
def given_input_file():
    return read_file(INPUT_FILE_NAME)


def test_run_1_with_input(given_input_file):
    result_1, invalid_seqs = run_1(given_input_file[0], given_input_file[1])
    result_2 = run_2(given_input_file[0], invalid_seqs)

    assert result_1 == 5955
    assert result_2 == 4030
