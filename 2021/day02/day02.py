from dataclasses import dataclass
import pathlib

WORKDIR = str(pathlib.Path(__file__).parent.resolve())

# ----------- PART 1 -------------------
@dataclass
class Submarine:
    x: int = 0
    y: int = 0
    aim: int = 0

    def move(self, action, distance):
        if action == "forward":
            self.x += distance
        else:
            self.y += distance * (1 if action == "down" else -1)

    def get_coord_multiplied(self):
        return self.x * self.y


sub = Submarine()
with open(WORKDIR + "/input") as f:
    for i, line in enumerate(f):
        action, distance = line.strip().split(" ")
        sub.move(action, int(distance))

print(sub.get_coord_multiplied())

# ----------- PART 2 -------------------
@dataclass
class Submarine2:
    x: int = 0
    y: int = 0
    aim: int = 0

    def move(self, action, distance):
        if action == "forward":
            self.x += distance
            self.y += distance * self.aim
        else:
            self.aim += distance * (1 if action == "down" else -1)

    def get_coord_multiplied(self):
        return self.x * self.y


sub = Submarine2()
with open(WORKDIR + "/input") as f:
    for i, line in enumerate(f):
        action, distance = line.strip().split(" ")
        sub.move(action, int(distance))

print(sub.get_coord_multiplied())
