def read_string(filename: str) -> list[str]:
    input_string = []
    with open(filename, "r") as file:
        input_string = list("".join(x.strip() for x in file))

    return input_string
