import re

from utils import read_matrix

REGEX_XMAS = r"(?=(XMAS))|(?=(SAMX))"


def run_1(matrix: list[list[str]]) -> int:
    n_rows, n_cols = len(matrix), len(matrix[0])

    result = 0

    # horizonally
    for row_as_list in matrix:
        result += len(re.findall(REGEX_XMAS, "".join(row_as_list)))

    # vertically
    for i_col in range(n_cols):
        s = ""
        for i_row in range(n_rows):
            s += matrix[i_row][i_col]
        result += len(re.findall(REGEX_XMAS, s))

    # from top-left to bottom-right
    for start in range(n_rows + n_cols - 1):
        diag = []
        for row in range(n_rows):
            col = start - row
            if 0 <= col < n_cols:
                diag.append(matrix[row][col])

        result += len(re.findall(REGEX_XMAS, "".join(diag)))

    # from top-right to bottom-left
    for start in range(n_rows + n_cols - 1):
        diag = []
        for row in range(n_rows):
            col = start - (n_rows - 1 - row)
            if 0 <= col < n_cols:
                diag.append(matrix[row][col])

        result += len(re.findall(REGEX_XMAS, "".join(diag)))

    return result


def run_2(matrix: list[list[str]]) -> int:
    n_rows, n_cols = len(matrix), len(matrix[0])
    result = 0
    candidates = set(["MASSAM", "MASMAS", "SAMSAM", "SAMMAS"])

    for i in range(1, n_rows - 1):
        for j in range(1, n_cols - 1):
            x_cross = [
                matrix[i - 1][j - 1],  # top-left diagonal
                matrix[i][j],  # center
                matrix[i + 1][j + 1],  # bottom-right diagonal
                matrix[i - 1][j + 1],  # top-right diagonal
                matrix[i][j],  # center
                matrix[i + 1][j - 1],  # bottom-left diagonal
            ]
            if "".join(x_cross) in candidates:
                result += 1

    return result


if __name__ == "__main__":
    s = read_matrix("input.txt")
    r1 = run_1(s)
    print(r1)

    r2 = run_2(s)
    print(r2)
