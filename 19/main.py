from utils import read_input


def run(
    available_patterns: list[str], requested_designs: list[str], part_1: bool
) -> str:
    result = 0

    for design in requested_designs:
        result += dp(available_patterns, design, part_1, {})

    return result


def dp(available_patterns: list[str], towel: str, part_1: bool, memo):
    if len(towel) == 0:
        return 1

    if towel in memo:
        return memo[towel]

    res = 0
    for i in range(0, len(towel)):
        t = towel[0 : i + 1]
        if t in available_patterns:
            res += dp(available_patterns, towel[i + 1 :], part_1, memo)
            if part_1 and res == 1:
                return 1

    memo[towel] = res
    return res


if __name__ == "__main__":
    available_patterns, requested_designs = read_input("example_1.txt")
    # print(available_patterns)
    # print(requested_designs)

    r1 = run(available_patterns, requested_designs, True)
    print(r1)

    r2 = run(available_patterns, requested_designs, False)
    print(r2)
