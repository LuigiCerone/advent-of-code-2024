from utils import read_string


def run_1(compact_disk: list[str]) -> int:
    expanded_disk = expand_disk_map(compact_disk)

    optimized_disk = optimize_disk_map(expanded_disk)

    checksum = compute_checksum(optimized_disk)
    return checksum


def expand_disk_map(compressed_disk: list[str]):
    expanded = []
    current_id = 0
    space_part = False

    for item in compressed_disk:
        if space_part:
            for _ in range(int(item)):
                expanded.append(".")
        else:
            for _ in range(int(item)):
                expanded.append(f"{current_id}")
            current_id += 1
        space_part = not space_part

    return expanded


def optimize_disk_map(expanded_disk: list[str]):
    left, right = 0, len(expanded_disk) - 1

    while left < right:
        while expanded_disk[left] != ".":
            left += 1
        while expanded_disk[right] == ".":
            right -= 1

        expanded_disk[left] = expanded_disk[right]
        expanded_disk[right] = "."

        left += 1
        right -= 1

    return expanded_disk


def compute_checksum(optimized_disk: list[str]):
    result = 0
    valid = [e for e in optimized_disk if e != "."]

    for index, id in enumerate(valid):
        if id == ".":
            continue
        result = result + (index * int(id))

    return result


def run_2(compact_disk: list[str]) -> int:
    busy, free = expand_disk_map_2(compact_disk)

    new_busy = optimize_disk_map_2(busy, free)

    checksum = compute_checksum_2(new_busy)
    return checksum


def compute_checksum_2(busy):
    res = 0
    for k, (start, end) in busy.items():
        res += sum(k * i for i in range(start, end))

    return res


def expand_disk_map_2(compat_disk: list[str]) -> int:
    busy = {}
    free = []

    current_id = 0
    counter = 0
    free_part = False

    for value in compat_disk:
        start, end = counter, counter + int(value)

        if free_part:
            free.append((start, end))
        else:
            busy[current_id] = (start, end)
            current_id += 1

        free_part = not free_part
        counter += int(value)

    return busy, free


def optimize_disk_map_2(busy, free):
    current_file_id = max(busy.keys())

    while current_file_id >= 0:
        file_start, file_end = busy[current_file_id]
        file_len = file_end - file_start

        free_ptr = 0
        while free_ptr < len(free):
            free_start, gap_end = free[free_ptr]

            # skip free spaces that are irrelevant to the file’s placement
            if free_start >= file_start:
                break

            gap_len = gap_end - free_start
            if file_len <= gap_len:
                free.pop(free_ptr)

                new_file_start, new_file_end = free_start, free_start + file_len
                new_free_start, new_gap_end = new_file_end, gap_end

                busy[current_file_id] = (new_file_start, new_file_end)
                if new_free_start != new_gap_end:
                    free.insert(free_ptr, (new_free_start, new_gap_end))
                break
            else:
                # free space is not big enough
                free_ptr += 1

        current_file_id -= 1

    return busy


if __name__ == "__main__":
    input_string = read_string("input.txt")

    r1 = run_1(input_string)
    print(r1)

    r2 = run_2(input_string)
    print(r2)
