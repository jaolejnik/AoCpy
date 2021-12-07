import pathlib
from collections import Counter

WORKDIR = str(pathlib.Path(__file__).parent.resolve())

# ----------- PART 1 -------------------
with open(WORKDIR + "/input") as f:
    sub_positions = list(map(int, f.readline().split(",")))


target_pos = float("inf")
min_cost = float("inf")
for target in range(min(sub_positions), max(sub_positions)):
    cost = sum([abs(target - pos) for pos in sub_positions])
    if cost < min_cost:
        target_pos = target
        min_cost = cost

print(min_cost)

# ----------- PART 2 -------------------
target_pos = float("inf")
min_cost = float("inf")
for target in range(min(sub_positions), max(sub_positions)):
    cost = sum(
        [sum([x for x in range(1, abs(target - pos) + 1)]) for pos in sub_positions]
    )
    if cost < min_cost:
        target_pos = target
        min_cost = cost

print(min_cost)
