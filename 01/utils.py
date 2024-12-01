def read_arrays(filename: str) -> list[str]:
    list_a, list_b = list(), list()
    with open(filename, "r") as file:
        for line in file:
            values = line.strip().split()
            list_a.append(int(values[0]))
            list_b.append(int(values[1]))

    return list_a, list_b
