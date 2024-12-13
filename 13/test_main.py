import pytest

from main import run, find_solution
from utils import read_machines

INPUT_FILE_NAME: str = "input.txt"
EXAMPLE_FILE_NAME: str = "example_2.txt"


@pytest.fixture
def given_input_file():
    return read_machines(INPUT_FILE_NAME)


@pytest.fixture
def given_example_file():
    return read_machines(EXAMPLE_FILE_NAME)


def test_run_1_input_file_ok(given_input_file):
    tokens_required = run(given_input_file, True)

    assert tokens_required == 29517


def test_run_2_input_file_ok(given_input_file):
    tokens_required = run(given_input_file, False)

    assert tokens_required == 103570327981381


def test_find_solutions_works_with_input_ok():
    A = (94, 34)
    B = (22, 67)
    P = (8400, 5400)
    result = find_solution(A, B, P)

    assert result.solvable

    assert result.k == 80
    assert result.m == 40


def test_find_solutions_doesnt_work_with_input_ok():
    A = (2, 2)
    B = (4, 4)
    P = (13, 13)
    result = find_solution(A, B, P)

    assert not result.solvable
