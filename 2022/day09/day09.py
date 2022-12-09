import pathlib
import numpy as np

WORKDIR = str(pathlib.Path(__file__).parent.resolve())


class Knot:
    def __init__(self):
        self.visited_pos = []
        self.pos = np.array([0.0, 0.0])

        self.visited_pos.append(tuple(self.pos))

    def move(self, vec):
        self.pos += vec

        new_pos = tuple(self.pos)
        if new_pos not in self.visited_pos:
            self.visited_pos.append(tuple(self.pos))

    def __str__(self):
        return f"X: {self.pos[0]:02}, Y: {self.pos[1]:02}"


def move_head(head_knot, direction):
    match direction:
        case "U":
            vec = np.array((0.0, 1.0))
        case "D":
            vec = np.array((0.0, -1.0))
        case "R":
            vec = np.array((1.0, 0.0))
        case "L":
            vec = np.array((-1.0, 0.0))
        case _:
            print("Undefined direction")
            exit()

    head_knot.move(vec)


def move_tail(tail_knot, head_pos):
    dist_vec = head_pos - tail_knot.pos
    x_abs_dist = abs(dist_vec[0])
    y_abs_dist = abs(dist_vec[1])

    if x_abs_dist > 1 or y_abs_dist > 1:
        vec = np.array(
            (
                dist_vec[0] / max(x_abs_dist, 1),
                dist_vec[1] / max(y_abs_dist, 1),
            )
        )
        tail_knot.move(vec)

        return True

    return False


class Rope:
    def __init__(self, length):
        self.knots = [Knot() for _ in range(length)]

    def move(self, direction, steps):
        for _ in range(int(steps)):
            prev_knot = None
            for knot in self.knots:
                if prev_knot is None:
                    move_head(self.knots[0], direction)
                else:
                    moved = move_tail(knot, prev_knot.pos)
                    if not moved:
                        break
                prev_knot = knot


# ----------- PART 1 -------------------
with open(WORKDIR + "/input") as f:
    instructions = [line.strip().split() for line in f]

rope = Rope(2)
for direction, steps in instructions:
    rope.move(direction, steps)

print("Part 1:", len(rope.knots[-1].visited_pos))
# ----------- PART 2 -------------------
rope = Rope(10)
for direction, steps in instructions:
    rope.move(direction, steps)

print("Part 2:", len(rope.knots[-1].visited_pos))
