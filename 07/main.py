from utils import read_input
from collections import defaultdict


def dfs_1(curr_index, curr_result, dp, seq):
    dp[curr_index].add(curr_result)

    if curr_index == len(seq):
        return

    dfs_1(curr_index + 1, curr_result * seq[curr_index], dp, seq)

    dfs_1(curr_index + 1, curr_result + seq[curr_index], dp, seq)


def run_1(results: list[int], numbers: list[list[int]]) -> int:
    result = 0

    for i in range(len(results)):
        dp = defaultdict(set)
        target, seq = results[i], numbers[i]
        dfs_1(0, 0, dp, seq)

        if target in dp[len(seq)]:
            result += target

    return result


def dfs_2(curr_index, curr_result, dp, seq):
    dp[curr_index].add(curr_result)

    if curr_index == len(seq):
        return

    dfs_2(curr_index + 1, curr_result * seq[curr_index], dp, seq)

    dfs_2(curr_index + 1, curr_result + seq[curr_index], dp, seq)

    dfs_2(curr_index + 1, int(str(curr_result) + str(seq[curr_index])), dp, seq)


def run_2(results: list[int], numbers: list[list[int]]) -> int:
    result = 0

    for i in range(len(results)):
        dp = defaultdict(set)
        target, seq = results[i], numbers[i]
        dfs_2(0, 0, dp, seq)

        if target in dp[len(seq)]:
            result += target

    return result


if __name__ == "__main__":
    results, numbers = read_input("input.txt")

    r1 = run_1(results, numbers)
    print(r1)

    r2 = run_2(results, numbers)
    print(r2)
