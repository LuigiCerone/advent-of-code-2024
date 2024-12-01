from collections import defaultdict
from utils import read_arrays


def run_1(list_a: list[int], list_b: list[int]) -> int:
    list_a.sort()
    list_b.sort()
    result = 0

    for index in range(len(list_a)):
        distance = abs(list_a[index] - list_b[index])
        result += distance

    return result


def run_2(list_a: list[int], list_b: list[int]) -> int:
    counter = defaultdict(int)
    result = 0

    for n in list_b:
        counter[n] += 1

    for n in list_a:
        result = result + (n * counter[n])

    return result


if __name__ == "__main__":
    a, b = read_arrays("input.txt")
    r1 = run_1(a, b)
    print(r1)

    r2 = run_2(a, b)
    print(r2)
