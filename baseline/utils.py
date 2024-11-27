def read_file(filename: str) -> list[str]:
    with open(filename, "r") as file:
        return [line.strip() for line in file]
