def read_input(filename: str) -> list[tuple]:
    available_patterns, requested_designs = [], []

    with open(filename, "r") as file:
        content = file.read().split("\n\n")

        available_patterns = content[0].split(", ")

        requested_designs = content[1].split("\n")

    return available_patterns, requested_designs
