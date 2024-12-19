def read_input(filename: str) -> list[tuple]:
    input_result = []
    with open(filename, "r") as file:
        for line in file:
            input_result.append(tuple(map(int, line.strip().split(","))))

    return input_result
