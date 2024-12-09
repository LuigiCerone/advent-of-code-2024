from utils import read_matrix
from collections import defaultdict
from itertools import combinations


def run_1(antennas: defaultdict[str, tuple[int, int]], matrix: list[list[str]]) -> int:
    antinodes_set = set()

    for _, positions in antennas.items():
        combinations_result = list(combinations(positions, 2))

        for a, b in combinations_result:
            x1, y1 = a
            x2, y2 = b

            vector_x = x2 - x1
            vector_y = y2 - y1

            antinodes = [
                (x1 - vector_x, y1 - vector_y),  # Negative direction
                (x2 + vector_x, y2 + vector_y),  # Positive direction
            ]

            # Filter antinodes based on map bounds
            for x, y in antinodes:
                if is_in_matrix((x, y), matrix):
                    antinodes_set.add((round(x), round(y)))

    return len(antinodes_set)


def is_in_matrix(point, matrix):
    ROWS, COLS = len(matrix), len(matrix[0])
    return 0 <= point[0] < ROWS and 0 <= point[1] < COLS


def run_2(antennas: defaultdict[str, tuple[int, int]], matrix: list[list[str]]) -> int:
    antinodes_set = set()

    for _, positions in antennas.items():
        combinations_result = list(combinations(positions, 2))

        for a, b in combinations_result:
            x1, y1 = a
            x2, y2 = b

            vector_x = x2 - x1
            vector_y = y2 - y1

            i = 0
            while True:
                # Positive direction
                x_pos = x1 + i * vector_x
                y_pos = y1 + i * vector_y

                # Negative direction
                x_neg = x2 - i * vector_x
                y_neg = y2 - i * vector_y

                # Filter antinodes based on map bounds
                if is_in_matrix((x_pos, y_pos), matrix):
                    antinodes_set.add((int(x_pos), int(y_pos)))
                if is_in_matrix((x_neg, y_neg), matrix):
                    antinodes_set.add((int(x_neg), int(y_neg)))

                if not is_in_matrix((x_pos, y_pos), matrix) and not is_in_matrix(
                    (x_neg, y_neg), matrix
                ):
                    break

                i += 1

    return len(antinodes_set)


def compute_antennas(matrix: list[list[str]]):
    antennas = defaultdict(list)

    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] != ".":
                antennas[matrix[r][c]].append((r, c))

    return antennas


if __name__ == "__main__":
    matrix = read_matrix("input.txt")

    antenna_positions = compute_antennas(matrix)

    r1 = run_1(antenna_positions, matrix)
    print(r1)

    r2 = run_2(antenna_positions, matrix)
    print(r2)
