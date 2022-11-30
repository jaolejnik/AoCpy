import pathlib
import numpy as np

WORKDIR = str(pathlib.Path(__file__).parent.resolve())


with open(WORKDIR + "/input") as f:
    data = [l.strip() for l in f.readlines()]


stringified_data = "; ".join([" ".join([digit for digit in row]) for row in data])
matrix = np.array(np.mat(stringified_data))

# ----------- PART 1 -------------------
def flash_octopus(matrix, current_pos):
    matrix[current_pos] += 1

    dimx, dimy = matrix.shape
    neighbour_vectors = []
    if current_pos[0] > 0:
        neighbour_vectors.append(np.array((-1, 0)))
    if current_pos[0] < dimx - 1:
        neighbour_vectors.append(np.array((1, 0)))
    if current_pos[1] > 0:
        neighbour_vectors.append(np.array((0, -1)))
    if current_pos[1] < dimy - 1:
        neighbour_vectors.append(np.array((0, 1)))
    if current_pos[0] > 0 and current_pos[1] > 0:
        neighbour_vectors.append(np.array((-1, -1)))
    if current_pos[0] < dimx - 1 and current_pos[1] < dimy - 1:
        neighbour_vectors.append(np.array((1, 1)))
    if current_pos[0] > 0 and current_pos[1] < dimy - 1:
        neighbour_vectors.append(np.array((-1, 1)))
    if current_pos[0] < dimx - 1 and current_pos[1] > 0:
        neighbour_vectors.append(np.array((1, -1)))

    for nv in neighbour_vectors:
        matrix[tuple(np.array(current_pos) + nv)] += 1


def find_high_level_octopuses(matrix):
    result = np.where(matrix > 9)
    return set(zip(result[0], result[1]))


def resolve_step(matrix):
    ones = np.ones(matrix.shape).astype(int)
    matrix += ones
    high_level_octopuses = find_high_level_octopuses(matrix)
    already_flashed = set()

    while len(high_level_octopuses) - len(already_flashed) > 0:
        for octopus_pos in high_level_octopuses:
            if octopus_pos in already_flashed:
                continue
            flash_octopus(matrix, octopus_pos)

        already_flashed.update(high_level_octopuses)
        high_level_octopuses.update(find_high_level_octopuses(matrix))

    for octopus_pos in high_level_octopuses:
        matrix[octopus_pos] = 0

    flashes = len(high_level_octopuses)

    return flashes


total_flashes = 0
for step in range(100):
    total_flashes += resolve_step(matrix)
print(total_flashes)

# ----------- PART 2 -------------------
matrix = np.array(np.mat(stringified_data))
flash_count = 0
step = 0
while flash_count != np.product(matrix.shape):
    flash_count = resolve_step(matrix)
    step += 1

print(step)
