from dataclasses import dataclass

import re


BUTTON_PATTERN = r"Button (\w): X\+(\d+), Y\+(\d+)"
PRIZE_PATTERN = r"Prize: X=(\d+), Y=(\d+)"


@dataclass
class MachineInput:
    a: tuple[int, int]
    b: tuple[int, int]
    p: tuple[int, int]


def read_machines(filename: str) -> list[str]:
    input_list = []
    with open(filename, "r") as file:
        content = file.read()

        unparsed_machines = content.split("\n\n")

        for um in unparsed_machines:
            buttons = re.findall(BUTTON_PATTERN, um)
            button_data = {button.lower(): (int(x), int(y)) for button, x, y in buttons}

            prize_match = re.search(PRIZE_PATTERN, um)
            if prize_match:
                prize_data = {
                    "p": (int(prize_match.group(1)), int(prize_match.group(2)))
                }
            else:
                prize_data = {}

            input_list.append(MachineInput(**button_data, **prize_data))

    return input_list
