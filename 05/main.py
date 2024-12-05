from utils import read_file
from functools import cmp_to_key


def run_1(rules: list[int], sequences: list[int]) -> int:
    result = 0
    invalid_sequences = []

    for seq in sequences:
        if is_valid_seq(rules, seq):
            result += seq[len(seq) // 2]
        else:
            invalid_sequences.append(seq)

    return result, invalid_sequences


def is_valid_seq(rules: list[int], seq: list[int]):
    return all(seq.index(a) < seq.index(b) for a, b in rules if a in seq and b in seq)


def run_2(rules: list[int], invalid_sequences: list[int]) -> int:
    result = 0

    def cmp(p, q):
        return -1 if [p, q] in rules else 0

    for seq in invalid_sequences:
        sorted_seq = sorted(seq, key=cmp_to_key(cmp))
        result += sorted_seq[len(sorted_seq) // 2]

    return result


if __name__ == "__main__":
    rules, sequences = read_file("input.txt")
    r1, invalid_sequences = run_1(rules, sequences)
    print(r1)

    r2 = run_2(rules, invalid_sequences)
    print(r2)
