def read_input(filename: str) -> list[str]:
    results, numbers = [], []
    with open(filename, "r") as file:
        for line in file:
            colon_split = line.split(":")
            results.append(int(colon_split[0]))

            values = list(map(int, colon_split[1].strip().split(" ")))
            numbers.append(values)

    return results, numbers
