import copy
from utils import read_matrix
from collections import defaultdict

GUARD_DIRECTIONS = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}

NEXT_GUARD_DIRECTION = {"^": ">", ">": "v", "v": "<", "<": "^"}


def turn_guard(current_guard_direction: str) -> str:
    return NEXT_GUARD_DIRECTION[current_guard_direction]


def is_in_matrix(r: int, c: int, matrix: list[list[str]]) -> bool:
    return 0 <= r < len(matrix) and 0 <= c < len(matrix[0])


def run_1(matrix: list[list[str]]) -> set[tuple[str, str]]:
    r, c = get_starting_position(matrix)

    current_guard_direction = "^"
    exit_matrix = False
    position_visited = set([(r, c)])

    while not exit_matrix:
        while True:
            dr, dc = GUARD_DIRECTIONS[current_guard_direction]
            next_r, next_c = r + dr, c + dc

            if not is_in_matrix(next_r, next_c, matrix):
                exit_matrix = True
                break
            elif matrix[next_r][next_c] == "#":
                current_guard_direction = turn_guard(current_guard_direction)
                continue

            r, c = next_r, next_c
            position_visited.add((r, c))

    return position_visited


def check_for_loop(matrix: list[list[str]]):
    r, c = get_starting_position(matrix)

    current_guard_direction = "^"
    exit_matrix = False
    pass_count = defaultdict(int)
    pass_count[(r, c)] += 1

    while not exit_matrix:
        while True:
            dr, dc = GUARD_DIRECTIONS[current_guard_direction]
            next_r, next_c = r + dr, c + dc

            if not is_in_matrix(next_r, next_c, matrix):
                exit_matrix = True
                break
            elif matrix[next_r][next_c] == "#" or matrix[next_r][next_c] == "0":
                current_guard_direction = turn_guard(current_guard_direction)
                continue

            r, c = next_r, next_c
            pass_count[(r, c)] += 1

            if pass_count[(r, c)] == 10:
                return True

    return False


def run_2(matrix: list[list[str]], positions_visited: set[tuple[str, str]]):
    result = 0

    start_r, start_c = get_starting_position(matrix)
    positions_visited.remove((start_r, start_c))

    for r, c in positions_visited:
        matrix_copy = copy.deepcopy(matrix)

        # Add an obstacle
        matrix_copy[r][c] = "0"

        # Check if guard step on it
        result += int(check_for_loop(matrix_copy))

    return result


def get_starting_position(matrix: list[list[str]]):
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == "^":
                return r, c


if __name__ == "__main__":
    matrix = read_matrix("input.txt")
    positions_visited = run_1(matrix)
    print(len(positions_visited))

    r2 = run_2(matrix, positions_visited)
    print(r2)
