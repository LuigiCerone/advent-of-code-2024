def read_int_list(filename: str) -> list[str]:
    input_list = []
    with open(filename, "r") as file:
        input_list = list(map(int, file.read().strip().split()))

    return input_list
