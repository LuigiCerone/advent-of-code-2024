from utils import read_matrix
from collections import defaultdict

ALLOWED_DIRECTIONS = [(1, 0, "D"), (-1, 0, "U"), (0, 1, "R"), (0, -1, "L")]


def is_in_matrix(point: tuple[int, int], matrix: list[list[str]]):
    x, y = point
    return 0 <= x < len(matrix) and 0 <= y < len(matrix[0])


def find_all_areas(matrix: list[list[str]]):
    visited_set = set()
    ROWS, COLS = len(matrix), len(matrix[0])
    areas = defaultdict(list)

    for r in range(ROWS):
        for c in range(COLS):
            if (r, c) not in visited_set:
                new_area = find_area_points(matrix, r, c, visited_set, [(r, c)])

                areas[matrix[r][c]].append(new_area)

    return areas


def run(matrix: list[list[str]], part_1: bool) -> int:
    areas = find_all_areas(matrix)

    result = 0

    for plant_areas in areas.values():
        for plant_area in plant_areas:
            area = len(plant_area)

            if part_1:
                perimeter = compute_perimeter(plant_area)
                result += area * perimeter
            else:
                num_sides = compute_sides(plant_area)
                result += area * num_sides

    return result


def find_area_points(
    matrix: list[list[str]],
    r: int,
    c: int,
    visited_set: set,
    curr_area: list[tuple[int, int]],
) -> list[tuple[int, int]]:
    visited_set.add((r, c))

    for dr, dc, _ in ALLOWED_DIRECTIONS:
        nr, nc = r + dr, c + dc

        if (
            (nr, nc) not in visited_set
            and is_in_matrix((nr, nc), matrix)
            and matrix[r][c] == matrix[nr][nc]
        ):
            curr_area.append((nr, nc))
            find_area_points(matrix, nr, nc, visited_set, curr_area)

    return curr_area


def compute_perimeter(area: list[tuple[int, int]]) -> int:
    perimeter = 0
    area_set = set(area)

    for r, c in area:
        for dr, dc, _ in ALLOWED_DIRECTIONS:
            neighbor = (r + dr, c + dc)

            # If not in the set, it means it is an exposed side
            if neighbor not in area_set:
                perimeter += 1

    return perimeter


def compute_sides(area: list[tuple[int, int]]) -> int:
    area_set = set(area)

    left = set()
    right = set()
    up = set()
    down = set()

    for r, c in area:
        for dr, dc, direction in ALLOWED_DIRECTIONS:
            neighbor = (r + dr, c + dc)
            if neighbor not in area_set:
                if direction == "U":
                    up.add((r, c))
                elif direction == "D":
                    down.add((r, c))
                elif direction == "L":
                    left.add((r, c))
                elif direction == "R":
                    right.add((r, c))

    corners = 0
    for r, c in up:
        if (r, c) in left:
            corners += 1
        if (r, c) in right:
            corners += 1
        if (r - 1, c - 1) in right and (r, c) not in left:
            corners += 1
        if (r - 1, c + 1) in left and (r, c) not in right:
            corners += 1

    for r, c in down:
        if (r, c) in left:
            corners += 1
        if (r, c) in right:
            corners += 1
        if (r + 1, c - 1) in right and (r, c) not in left:
            corners += 1
        if (r + 1, c + 1) in left and (r, c) not in right:
            corners += 1

    return corners


if __name__ == "__main__":
    input_matrix = read_matrix("input.txt")

    r1 = run(input_matrix, use_perimeter=True)
    print(r1)

    r2 = run(input_matrix, use_perimeter=False)
    print(r2)
