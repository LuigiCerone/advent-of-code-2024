from utils import read_input

SIMULATE_BYTES = 1024
MAX_MAP_SIZE = 71
ALLOWED_DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def run_1(corrupted_bytes: list[tuple[int, int]]) -> str:
    start_position = (0, 0)
    end_position = (MAX_MAP_SIZE - 1, MAX_MAP_SIZE - 1)

    visited = set()

    queue = [(start_position, (1, 0), 0), (start_position, (0, 1), 0)]

    while queue:
        current_position, current_direction, steps = queue.pop(0)
        visited.add(current_position)

        if current_position == end_position:
            return steps
            break

        x, y = current_position

        for direction in ALLOWED_DIRECTIONS:
            dx, dy = direction
            nx, ny = (x + dx), (y + dy)

            if nx < 0 or nx >= MAX_MAP_SIZE or ny < 0 or ny >= MAX_MAP_SIZE:
                continue

            # avoid reverse movement
            if current_direction[0] * dx + current_direction[1] * dy < 0:
                continue

            if (nx, ny) in visited:
                continue

            if (nx, ny) in corrupted_bytes:
                continue

            item = ((nx, ny), direction, steps + 1)
            if item in queue:
                continue

            queue.append(item)


def run_2(matrix: list[list[str]]) -> int:
    pass


def get_corrupted_bytes(
    falling_bytes: list[tuple[int, int]], cut_size: int
) -> set[tuple[int, int]]:
    return set(falling_bytes[:cut_size])


if __name__ == "__main__":
    falling_bytes = read_input("input.txt")
    corrupted_bytes = get_corrupted_bytes(falling_bytes, cut_size=SIMULATE_BYTES)
    # print(corrupted_bytes)

    r1 = run_1(corrupted_bytes)
    print(r1)

    # r2 = run_2(input_matrix)
    # print(r2)
