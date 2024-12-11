from utils import read_int_list

NUMBER_BLINKS_PART_1 = 25
NUMBER_BLINKS_PART_2 = 75


def run(stones: list[int], max_num_blinks: int) -> int:
    return sum(count_stones(s, max_num_blinks, {}) for s in stones)


def process_stone(stone: int) -> list[int]:
    if stone == 0:
        return [1]

    stone_as_str = str(stone)

    if len(stone_as_str) % 2 == 0:
        half = len(stone_as_str) // 2
        return [int(stone_as_str[:half]), int(stone_as_str[half:])]
    else:
        return [stone * 2024]


def count_stones(value: int, count: int, dp: dict):
    # base case
    if count == 0:
        return 1

    # cache check
    if (value, count) in dp:
        return dp[(value, count)]

    next_step_stones = process_stone(value)

    # recursive calculation with memoization
    dp[(value, count)] = sum(
        count_stones(stone, count - 1, dp) for stone in next_step_stones
    )
    return dp[(value, count)]


if __name__ == "__main__":
    input_stones = read_int_list("input.txt")

    r1 = run(input_stones, NUMBER_BLINKS_PART_1)
    print(r1)

    r2 = run(input_stones, NUMBER_BLINKS_PART_2)
    print(r2)
