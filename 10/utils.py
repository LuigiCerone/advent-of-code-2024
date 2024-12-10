def read_matrix(filename: str) -> list[str]:
    matrix = []
    with open(filename, "r") as file:
        for line in file:
            values = list(map(int, line.strip()))
            matrix.append(values)

    return matrix
