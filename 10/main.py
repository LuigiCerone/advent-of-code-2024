from utils import read_matrix

ALLOWED_DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def run(matrix: list[list[int]], part_one: bool) -> int:
    result = 0
    starts = find_starting_points(matrix)

    for start_x, start_y in starts:
        score = dfs_explore_map((start_x, start_y), matrix)
        if part_one:
            result += len(set(score))
        else:
            result += len(score)

    return result


def dfs_explore_map(
    current_point: tuple[int, int], matrix: list[list[int]]
) -> list[tuple[int, int]]:
    result = []
    curr_x, curr_y = current_point[0], current_point[1]

    if matrix[curr_x][curr_y] == 9:
        return [(curr_x, curr_y)]

    for dx, dy in ALLOWED_DIRECTIONS:
        next_x = curr_x + dx
        next_y = curr_y + dy

        if (
            is_in_matrix((next_x, next_y), matrix)
            and matrix[next_x][next_y] == matrix[curr_x][curr_y] + 1
        ):
            result = result + dfs_explore_map((next_x, next_y), matrix)

    return result


def is_in_matrix(point: tuple[int, int], matrix: list[list[int]]) -> bool:
    return 0 <= point[0] < len(matrix) and 0 <= point[1] < len(matrix[0])


def find_starting_points(matrix: list[list[int]]) -> list[tuple[int, int]]:
    starts = []

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0:
                starts.append((row, col))

    return starts


if __name__ == "__main__":
    matrix = read_matrix("input.txt")

    r1 = run(matrix, part_one=True)
    print(r1)

    r2 = run(matrix, part_one=False)
    print(r2)
