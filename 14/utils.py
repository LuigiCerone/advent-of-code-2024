from dataclasses import dataclass

import re


@dataclass
class Robot:
    position: tuple[int, int]
    velocity: tuple[int, int]


POSITION_PATTERN = r"p=(-?\d+),(-?\d+)"
VELOCITY_PATTERN = r"v=(-?\d+),(-?\d+)"


def read_input(filename: str) -> list[Robot]:
    input_list = []
    with open(filename, "r") as file:
        for line in file:
            position_match = re.search(POSITION_PATTERN, line)
            velocity_match = re.search(VELOCITY_PATTERN, line)

            point = (int(position_match.group(1)), int(position_match.group(2)))
            velocity = (int(velocity_match.group(1)), int(velocity_match.group(2)))

            input_list.append(Robot(point, velocity))

    return input_list
