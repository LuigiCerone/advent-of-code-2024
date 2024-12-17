import math

from utils import Registers, read_input


def resolve_combo_operand(operand, registers: Registers):
    if 0 <= operand <= 3:
        return operand
    elif operand == 4:
        return registers.register_a
    elif operand == 5:
        return registers.register_b
    elif operand == 6:
        return registers.register_c


def compute_step(registers: Registers, opcode: int, operand: int) -> tuple[str, int]:
    if opcode == 0:
        registers.register_a = math.trunc(
            registers.register_a
            / math.pow(2, resolve_combo_operand(operand, registers))
        )
    elif opcode == 1:
        registers.register_b = registers.register_b ^ operand
    elif opcode == 2:
        registers.register_b = resolve_combo_operand(operand, registers) % 8
    elif opcode == 3:
        if registers.register_a == 0:
            return "", -1
        return "", operand
    elif opcode == 4:
        registers.register_b = registers.register_b ^ registers.register_c
    elif opcode == 5:
        result = resolve_combo_operand(operand, registers) % 8
        return str(result), -1
    elif opcode == 6:
        registers.register_b = math.trunc(
            registers.register_a
            / math.pow(2, resolve_combo_operand(operand, registers))
        )
    elif opcode == 7:
        registers.register_c = math.trunc(
            registers.register_a
            / math.pow(2, resolve_combo_operand(operand, registers))
        )

    return None, -1


def run_1(registers: Registers, program_input: list[tuple[int, int]]) -> str:
    result = ""

    pointer = 0

    while pointer < len(program_input):
        opcode, operand = program_input[pointer]

        output, new_pointer = compute_step(registers, opcode, operand)

        result += output if output else ""
        pointer = new_pointer if new_pointer != -1 else pointer + 1

    return ",".join(list(result))


def run_2(matrix: list[list[str]]) -> int:
    pass


if __name__ == "__main__":
    input_registers, program_steps = read_input("input.txt")
    # print(input_registers)
    # print(program_steps)

    r1 = run_1(input_registers, program_steps)
    print(r1)  # 4,3,7,1,5,3,0,5,4

    # r2 = run_2(input_matrix)
    # print(r2)
