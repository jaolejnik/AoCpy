import pathlib
import numpy as np

WORKDIR = str(pathlib.Path(__file__).parent.resolve())

# ----------- PART 1 -------------------
def find_low_points(matrix):
    low_points = []

    dimx, dimy = matrix.shape
    for x in range(dimx):
        for y in range(dimy):
            neighbour_vectors = []
            if x > 0:
                neighbour_vectors.append(np.array((-1, 0)))
            if x < dimx - 1:
                neighbour_vectors.append(np.array((1, 0)))
            if y > 0:
                neighbour_vectors.append(np.array((0, -1)))
            if y < dimy - 1:
                neighbour_vectors.append(np.array((0, 1)))

            neighbours = [
                matrix[tuple(np.array((x, y)) + nv)] for nv in neighbour_vectors
            ]
            bigger_neighbour_count = sum(
                [matrix[x, y] < neighbour for neighbour in neighbours]
            )
            if bigger_neighbour_count == len(neighbours):
                low_points.append({"value": matrix[x, y], "pos": (x, y)})

    return low_points


with open(WORKDIR + "/input") as f:
    data = [l.strip() for l in f.readlines()]


stringified_data = "; ".join([" ".join([digit for digit in row]) for row in data])
matrix = np.array(np.mat(stringified_data))


dimx, dimy = matrix.shape
low_points = find_low_points(matrix)

print(sum([lp["value"] + 1 for lp in low_points]))

# ----------- PART 2 -------------------


def find_basin(matrix, prev_value, current_pos, visited):
    if (
        current_pos in visited
        or prev_value
        and matrix[current_pos] < prev_value
        or matrix[current_pos] == 9
    ):
        return 0

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

    counter = 1
    visited.append(current_pos)
    for nv in neighbour_vectors:
        counter += find_basin(
            matrix,
            matrix[current_pos],
            tuple(
                np.array(current_pos) + nv,
            ),
            visited,
        )

    return counter


basin_sizes = [find_basin(matrix, None, lp["pos"], []) for lp in low_points]
basin_sizes.sort()
print(np.product(basin_sizes[-3:]))
