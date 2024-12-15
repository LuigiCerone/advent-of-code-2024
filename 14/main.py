from utils import Robot, read_input
from itertools import count
from copy import deepcopy

N_ROWS, N_COLS = 101, 103

PART_1_SECONDS = 100


def run_1(input_positions: list[int], num_secs: int, n_rows, n_cols) -> int:
    robots_positions = input_positions

    move_robots(robots_positions, num_secs, n_rows, n_cols)

    return count_quadrants(robots_positions)


def count_quadrants(positions: list[Robot]):
    quadrants = [0] * 4

    for robot in positions:
        x_robot, y_robot = robot.position

        if x_robot < 50 and y_robot < 51:
            quadrants[0] += 1
        elif x_robot > 50 and y_robot < 51:
            quadrants[1] += 1
        elif x_robot < 50 and y_robot > 51:
            quadrants[2] += 1
        elif x_robot > 50 and y_robot > 51:
            quadrants[3] += 1

    return quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]


def move_robots(positions: list[Robot], step, n_rows, n_cols):
    for robot in positions:
        x_robot, y_robot = robot.position
        x_velocity, y_velocity = robot.velocity

        new_x_robot = (x_robot + (step * x_velocity)) % n_rows
        new_y_robot = (y_robot + (step * y_velocity)) % n_cols

        robot.position = (new_x_robot, new_y_robot)


def generate_map(positions: list[Robot], n_rows, n_cols):
    map = [["0" for _ in range(n_cols)] for _ in range(n_rows)]

    for robot in positions:
        x, y = robot.position

        map[x][y] = "1"

    return map


def find_sequence(map: list[list[str]], n_rows, n_cols, target_len):
    seq = 0

    for r in range(n_rows):
        for c in range(n_cols):
            if map[r][c] == "1":
                seq += 1
            elif map[r][c] == "0":
                seq = 0

            if seq == target_len:
                return True

    return False


def run_2(input_positions: list[Robot], n_rows, n_cols) -> int:
    robots_positions = input_positions

    for second in count():
        move_robots(robots_positions, 1, n_rows, n_cols)

        map_as_list = generate_map(robots_positions, n_rows, n_cols)

        if find_sequence(map_as_list, n_rows, n_cols, 10):
            draw(robots_positions, n_rows, n_cols)
            return second


def draw(input_positions: list[Robot], n_rows, n_cols):
    grid = [["."] * n_cols for _ in range(n_rows)]
    for robot in input_positions:
        x, y = robot.position
        grid[x][y] = "\u2588"
    print("\n".join("".join(row) for row in grid))


if __name__ == "__main__":
    input_positions = read_input("input.txt")
    # print(input_positions)

    r1 = run_1(deepcopy(input_positions), PART_1_SECONDS, N_ROWS, N_COLS)
    print(r1)

    r2 = run_2(input_positions, N_ROWS, N_COLS)
    print(r2)
