import pytest

from main import process_row, process_row_2
from utils import read_matrix

INPUT_FILE_NAME: str = "input.txt"


@pytest.fixture
def given_input_file():
    return read_matrix(INPUT_FILE_NAME)


def test_process_row_delta_ok_with_valid_input():
    input_list = [1, 3, 5]
    result = process_row(input_list)

    expected_result = True

    assert result == expected_result


def test_process_row_delta_fails_with_invalid_input():
    input_list = [1, 3, 7]
    result = process_row(input_list)

    expected_result = False

    assert result == expected_result


def test_process_row_fails_with_wrong_order_input():
    input_list = [3, 2, 5]
    result = process_row(input_list)

    expected_result = False

    assert result == expected_result

    input_list = [3, 5, 2]
    result = process_row(input_list)

    expected_result = False

    assert result == expected_result


def test_process_row_2_fails_with_wrong_input():
    input_list = [1, 5, 3, 6, 5]
    result = process_row_2(input_list)

    expected_result = False

    assert result == expected_result


def test_process_row_2_ok_with_input_with_one_problem():
    input_list = [1, 9, 3]
    result = process_row_2(input_list)

    expected_result = True

    assert result == expected_result
