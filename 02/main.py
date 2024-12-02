from utils import read_matrix


def process_row(row: list[int]) -> bool:
    difference = row[0] - row[1]

    for index in range(1, len(row)):
        new_difference = row[index - 1] - row[index]

        if (
            new_difference == 0
            or abs(new_difference) > 3
            or (new_difference > 0) != (difference > 0)
        ):
            return False

    return True


def run_1(matrix: list[list[int]]) -> int:
    result = 0

    for row in matrix:
        result += int(process_row(row))

    return result


def process_row_2(row: list[int]) -> int:
    for i in range(len(row)):
        # Compute combination but exclude i-th element
        new_row = row[:i] + row[i + 1 :]

        if process_row(new_row):
            return True

    return False


def run_2(matrix: list[list[int]]) -> int:
    result = 0

    for row in matrix:
        result += int(process_row_2(row))

    return result


if __name__ == "__main__":
    m = read_matrix("input.txt")
    r1 = run_1(m)
    print(r1)

    r2 = run_2(m)
    print(r2)
