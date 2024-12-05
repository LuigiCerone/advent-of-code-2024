def read_file(filename: str) -> tuple[list[str], list[str]]:
    rules, sequences = [], []
    with open(filename, "r") as file:
        content = file.read()

    r, s = content.split("\n\n")

    for line in r.splitlines():
        values = list(map(int, line.strip().split("|")))
        rules.append(values)

    for line in s.splitlines():
        values = list(map(int, line.strip().split(",")))
        sequences.append(values)

    return rules, sequences
