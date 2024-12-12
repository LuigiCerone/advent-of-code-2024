def read_matrix(filename: str) -> list[str]:
    input_matrix = []
    with open(filename, "r") as file:
        for line in file:
            values = list(line.strip())
            input_matrix.append(values)

    return input_matrix
