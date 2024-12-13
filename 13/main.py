from typing import Optional
import numpy as np
from dataclasses import dataclass
from utils import read_machines

A_PRICE, B_PRICE = 3, 1
PART_2_INCREASE = 10000000000000


@dataclass
class Solution:
    solvable: bool
    k: Optional[int] = None
    m: Optional[int] = None


def run(machines: list[int], part_one: bool) -> int:
    result = 0

    for machine_run in machines:
        if not part_one:
            origin_p_value = machine_run.p
            machine_run.p = (
                origin_p_value[0] + PART_2_INCREASE,
                origin_p_value[1] + PART_2_INCREASE,
            )

        solution = find_solution(machine_run.a, machine_run.b, machine_run.p)

        if not solution.solvable:
            continue

        result += solution.k * 3 + solution.m

    return result


def is_close_to_integer(value, tolerance=1e-4):
    return abs(value - round(value)) < tolerance


def find_solution(
    A: tuple[int, int], B: tuple[int, int], P: tuple[int, int]
) -> Solution:
    # create the matrix and the target point vector
    coeff_matrix = np.array([[A[0], B[0]], [A[1], B[1]]])
    P_vector = np.array([P[0], P[1]])

    result = {}
    try:
        k_m = np.linalg.solve(coeff_matrix, P_vector)
        if all(is_close_to_integer(k) for k in k_m):
            result = Solution(True, int(round(k_m[0])), int(round(k_m[1])))
        else:
            result = Solution(False)
    except np.linalg.LinAlgError:
        # no solution
        result = Solution(False)

    return result


if __name__ == "__main__":
    input_machines = read_machines("input.txt")
    # print(input_machines)

    r1 = run(input_machines, part_one=True)
    print(r1)

    r2 = run(input_machines, part_one=False)
    print(r2)
