import heapq

from utils import read_matrix

DIRECTIONS = {"E": (0, 1), "W": (0, -1), "N": (-1, 0), "S": (1, 0)}
REVERSE_DIRECTIONS = {"E": "W", "W": "E", "N": "S", "S": "N"}


def run_1(matrix: list[list[str]]) -> int:
    start, end = get_start_end(matrix)

    start_r, start_c = start
    end_r, end_c = end

    dist = dijkstra(matrix, [(start_r, start_c, "E")])

    result = 10**10

    for dir in "EWNS":
        if (end_r, end_c, dir) in dist:
            result = min(result, dist[(end_r, end_c, dir)])
    return result


def dijkstra(matrix, starts):
    distances = {}

    pq = []
    for sr, sc, dir in starts:
        distances[(sr, sc, dir)] = 0
        heapq.heappush(pq, (0, sr, sc, dir))

    while pq:
        (cost, row, col, direction) = heapq.heappop(pq)

        if distances[(row, col, direction)] < cost:
            continue

        for next_dir in "EWNS".replace(direction, ""):
            if (row, col, next_dir) not in distances or distances[
                (row, col, next_dir)
            ] > cost + 1000:
                distances[(row, col, next_dir)] = cost + 1000
                heapq.heappush(pq, (cost + 1000, row, col, next_dir))

        dr, dc = DIRECTIONS[direction]
        next_row, next_col = row + dr, col + dc

        if (
            0 <= next_row < len(matrix)
            and 0 <= next_col < len(matrix[0])
            and matrix[next_row][next_col] != "#"
            and (
                (next_row, next_col, direction) not in distances
                or distances[(next_row, next_col, direction)] > cost + 1
            )
        ):
            distances[(next_row, next_col, direction)] = cost + 1
            heapq.heappush(pq, (cost + 1, next_row, next_col, direction))

    return distances


def run_2(matrix: list[list[str]]) -> int:
    start, end = get_start_end(matrix)

    start_r, start_c = start
    end_r, end_c = end

    distances_from_start = dijkstra(matrix, [(start_r, start_c, "E")])
    distances_from_end = dijkstra(matrix, [(end_r, end_c, d) for d in "EWNS"])

    optimal_cost = run_1(matrix)

    result = set()
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            for dir in "EWNS":
                current_from_start = (row, col, dir)
                current_from_end = (row, col, REVERSE_DIRECTIONS[dir])

                if (
                    current_from_start in distances_from_start
                    and current_from_end in distances_from_end
                ):
                    if (
                        distances_from_start[current_from_start]
                        + distances_from_end[current_from_end]
                        == optimal_cost
                    ):
                        result.add((row, col))
    return len(result)


def get_start_end(input_matrix: list[list[str]]):
    start, end = None, None

    for r in range(len(input_matrix)):
        for c in range(len(input_matrix[0])):
            if input_matrix[r][c] == "S":
                start = (r, c)
            if input_matrix[r][c] == "E":
                end = (r, c)

    return start, end


if __name__ == "__main__":
    input_matrix = read_matrix("input.txt")
    # print(input_matrix)

    r1 = run_1(input_matrix)
    print(r1)

    r2 = run_2(input_matrix)
    print(r2)
