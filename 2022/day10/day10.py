import pathlib
import copy

WORKDIR = str(pathlib.Path(__file__).parent.resolve())

# ----------- PART 1 -------------------
CYCLES_TO_PROCESS_SIGNAL = 2


with open(WORKDIR + "/input") as f:
    instructions = f.read().splitlines()


def get_signal_strengths(instructions, save_cycles):
    register = 1
    buffer = [0] * CYCLES_TO_PROCESS_SIGNAL
    signal_strengths = []

    cycle = 1
    while not (buffer_empty := is_buffer_empty(buffer)) or len(instructions) > 0:

        if buffer_empty:
            instruction = instructions.pop(0)
            execute_instruction(buffer, instruction)

        if cycle in save_cycles:
            signal_strengths.append(cycle * register)

        # print("\nCYCLE", cycle)
        # print(f"During: b={buffer} r={register}")
        register += advance_buffer(buffer)
        # print(f"After:  b={buffer} r={register}")

        cycle += 1

    return signal_strengths


def is_buffer_empty(buffer):
    return all(b == 0 for b in buffer)


def execute_instruction(buffer, instruction):
    command, *signal = instruction.split()
    if command == "addx":
        add_to_buffer(buffer, int(signal[0]))


def add_to_buffer(buffer, new_signal):
    buffer[-1] = new_signal


def advance_buffer(buffer):
    processed_signal = buffer[0]

    for i in range(1, len(buffer)):
        buffer[i - 1] = buffer[i]
    buffer[-1] = 0

    return processed_signal


cycles = [20, 60, 100, 140, 180, 220]
strengths = get_signal_strengths(copy.deepcopy(instructions), cycles)
print("Part 1:", sum(strengths))
# ----------- PART 2 -------------------
WIDTH = 40
HEIGHT = 6


def draw_to_screen(instructions, screen):
    sprite_pos = 1
    buffer = [0] * CYCLES_TO_PROCESS_SIGNAL

    cycle = 0
    while not (buffer_empty := is_buffer_empty(buffer)) or len(instructions) > 0:

        if buffer_empty:
            instruction = instructions.pop(0)
            execute_instruction(buffer, instruction)

        x = cycle % WIDTH
        y = cycle // WIDTH

        if sprite_pos - 1 <= x <= sprite_pos + 1:
            screen[y][x] = "#"

        sprite_pos += advance_buffer(buffer)

        cycle += 1


screen = [["." for _ in range(WIDTH)] for _ in range(HEIGHT)]
draw_to_screen(instructions, screen)

print("Part 2:")
for row in screen:
    print("".join(row))
