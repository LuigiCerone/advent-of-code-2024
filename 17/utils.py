from dataclasses import dataclass


@dataclass
class Registers:
    register_a: int
    register_b: int
    register_c: int


def read_input(filename: str) -> tuple[Registers, list[tuple]]:
    with open(filename, "r") as file:
        lines = file.read().strip().split("\n\n")

        # Parse registers
        registers_line = lines[0]
        registers_values = [
            int(value.split(": ")[1]) for value in registers_line.split("\n")
        ]
        register_a, register_b, register_c = registers_values

        # Parse program
        program_line = lines[1]
        program_values = list(map(int, program_line.split(": ")[1].split(",")))
        program_pairs = [
            (program_values[i], program_values[i + 1])
            for i in range(0, len(program_values), 2)
        ]

        return Registers(register_a, register_b, register_c), program_pairs
