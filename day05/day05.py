import pathlib
from dataclasses import dataclass
import numpy as np

WORKDIR = str(pathlib.Path(__file__).parent.resolve())


@dataclass
class Point:
    x: int
    y: int

    def get_tuple(self):
        return (self.x, self.y)


@dataclass
class Line:
    start: Point
    stop: Point


# ----------- PART 1 -------------------
def find_diagram_dim(lines):
    max_x = 0
    max_y = 0
    for line in lines:
        max_x = line.start.x if line.start.x > max_x else max_x
        max_x = line.stop.x if line.stop.x > max_x else max_x

        max_y = line.start.y if line.start.y > max_y else max_y
        max_y = line.stop.y if line.stop.y > max_y else max_y

    return max_x + 1, max_y + 1


lines = []
with open(WORKDIR + "/input") as f:
    for line in f:
        point1, point2 = [
            map(int, point.split(",")) for point in line.strip().split(" -> ")
        ]
        lines.append(Line(Point(*point1), Point(*point2)))

d_dim = find_diagram_dim(lines)
diagram = np.zeros(d_dim)

for line in lines:
    if line.start.x == line.stop.x or line.start.y == line.stop.y:
        x_coord = [line.start.x, line.stop.x]
        y_coord = [line.start.y, line.stop.y]
        x_coord.sort()
        y_coord.sort()

        range_x = range(x_coord[0], x_coord[1] + 1)
        range_y = range(y_coord[0], y_coord[1] + 1)

        for x in range_x:
            for y in range_y:
                diagram[y][x] += 1

counter = 0
for x in range(d_dim[0]):
    for y in range(d_dim[1]):
        counter += diagram[x][y] > 1

print(counter)

# ----------- PART 2 -------------------
diagram = np.zeros(d_dim)

for line in lines:
    x_coord = [line.start.x, line.stop.x]
    y_coord = [line.start.y, line.stop.y]

    if line.stop.x - line.start.x < 0:
        x_coord.sort()

    if line.stop.y - line.start.y < 0:
        y_coord.sort()

    range_x = list(range(x_coord[0], x_coord[1] + 1))
    range_y = list(range(y_coord[0], y_coord[1] + 1))

    if line.stop.x - line.start.x < 0:
        range_x.reverse()

    if line.stop.y - line.start.y < 0:
        range_y.reverse()

    if line.start.x == line.stop.x or line.start.y == line.stop.y:
        for x in range_x:
            for y in range_y:
                diagram[y][x] += 1

    elif abs(line.stop.x - line.start.x) == abs(line.stop.y - line.start.y):
        for x, y in zip(list(range_x), list(range_y)):
            diagram[y][x] += 1


counter = 0
for x in range(d_dim[0]):
    for y in range(d_dim[1]):
        counter += diagram[x][y] > 1

print(counter)
