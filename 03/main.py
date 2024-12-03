import re

from utils import read_string

REGEX_MUL = r"mul\(\d{1,3},\d{1,3}\)"
REGEX_MU_DO_DONT = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)"


def run_1(input_string: str) -> int:
    occurrences = re.finditer(REGEX_MUL, input_string)
    result = 0

    for item in occurrences:
        item = item.group()
        result = result + get_product(item)

    return result


def get_product(mul_as_str: str):
    numbers = list(
        map(
            int,
            mul_as_str[mul_as_str.index("(") + 1 : mul_as_str.index(")")].split(","),
        )
    )
    return numbers[0] * numbers[1]


def run_2(input_string: str) -> int:
    occurrences = re.finditer(REGEX_MU_DO_DONT, input_string)
    result = 0
    enabled = True

    for item in occurrences:
        item = item.group()

        if "do()" in item:
            enabled = True
        elif "don't()" in item:
            enabled = False
        elif enabled:
            result = result + get_product(item)

    return result


if __name__ == "__main__":
    s = read_string("input.txt")
    r1 = run_1(s)
    print(r1)

    r2 = run_2(s)
    print(r2)
