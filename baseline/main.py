def run(raw_input: list[str]):
    return [row.upper() for row in raw_input]


if __name__ == "__main__":
    print(run(["hello"]))
