import pytest

from main import expand_disk_map, optimize_disk_map, compute_checksum, run_1, run_2
from utils import read_string

INPUT_FILE_NAME: str = "input.txt"
EXAMPLE_FILE_NAME: str = "example.txt"


@pytest.fixture
def given_input_file():
    return read_string(INPUT_FILE_NAME)


@pytest.fixture
def given_example_file():
    return read_string(EXAMPLE_FILE_NAME)


def test_expand_disk_map_example_file(given_example_file):
    expanded_map = expand_disk_map(given_example_file)

    expected_result = [
        "0",
        "0",
        ".",
        ".",
        ".",
        "1",
        "1",
        "1",
        ".",
        ".",
        ".",
        "2",
        ".",
        ".",
        ".",
        "3",
        "3",
        "3",
        ".",
        "4",
        "4",
        ".",
        "5",
        "5",
        "5",
        "5",
        ".",
        "6",
        "6",
        "6",
        "6",
        ".",
        "7",
        "7",
        "7",
        ".",
        "8",
        "8",
        "8",
        "8",
        "9",
        "9",
    ]

    assert expanded_map == expected_result


def test_optimize_disk_map_example_file(given_example_file):
    expanded_map = expand_disk_map(given_example_file)
    optmized_map = optimize_disk_map(expanded_map)

    expected_result = [
        "0",
        "0",
        "9",
        "9",
        "8",
        "1",
        "1",
        "1",
        "8",
        "8",
        "8",
        "2",
        "7",
        "7",
        "7",
        "3",
        "3",
        "3",
        "6",
        "4",
        "4",
        "6",
        "5",
        "5",
        "5",
        "5",
        "6",
        "6",
        ".",
        ".",
        ".",
        ".",
        ".",
        ".",
        ".",
        ".",
        ".",
        ".",
        ".",
        ".",
        ".",
        ".",
    ]
    assert optmized_map == expected_result


def test_compute_checksum_example_file(given_example_file):
    expanded_map = expand_disk_map(given_example_file)
    optmized_map = optimize_disk_map(expanded_map)

    checksum = compute_checksum(optmized_map)

    assert checksum == 1928


def test_run_1_input_file_ok(given_input_file):
    checksum = run_1(given_input_file)

    assert checksum == 6320029754031


def test_run_2_input_file_ok(given_input_file):
    checksum = run_2(given_input_file)

    assert checksum == 6347435485773
