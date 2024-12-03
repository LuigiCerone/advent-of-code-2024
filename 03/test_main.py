import pytest

from main import run_1, run_2, get_product
from utils import read_string

INPUT_FILE_NAME: str = "input.txt"


@pytest.fixture
def given_input_file():
    return read_string(INPUT_FILE_NAME)


def test_run_1_with_input(given_input_file):
    result = run_1(given_input_file)

    expected_result = 173419328

    assert result == expected_result


def test_run_2_with_input(given_input_file):
    result = run_2(given_input_file)

    expected_result = 90669332

    assert result == expected_result


def test_get_product_ok_with_valid_input():
    mul_as_str = "mul(4,5)"

    assert get_product(mul_as_str) == 20
