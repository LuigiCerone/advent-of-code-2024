def read_matrix(filename: str) -> list[str]:
    matrix = []
    with open(filename, "r") as file:
        for line in file:
            values = list(map(int, line.strip().split()))
            matrix.append(values)

    return matrix
