def read_string(filename: str) -> list[str]:
    result: str = ""
    with open(filename, "r") as file:
        for line in file:
            result += line

    return result
