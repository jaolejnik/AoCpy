import pathlib
import numpy as np

WORKDIR = str(pathlib.Path(__file__).parent.resolve())

# ----------- PART 1 -------------------
with open(WORKDIR + "/input") as f:
    lanternfish = list(map(int, f.readline().strip().split(",")))

fish_to_add = 0
for day in range(80):
    fish_to_add = 0
    for i in range(len(lanternfish)):
        lanternfish[i] -= 1
        if lanternfish[i] == -1:
            fish_to_add += 1
            lanternfish[i] = 6

    for new_fish in range(fish_to_add):
        lanternfish.append(8)

print(len(lanternfish))

# ----------- PART 2 -------------------
# PART 1 was too slow, had to change the approach
lanternfish_counter = {i: 0 for i in range(9)}

with open(WORKDIR + "/input") as f:
    for day in list(map(int, f.readline().strip().split(","))):
        lanternfish_counter[day] += 1

for day in range(256):
    new_lanternfish = lanternfish_counter[0]
    for i in range(8):
        lanternfish_counter[i] = lanternfish_counter[i + 1]
    lanternfish_counter[6] += new_lanternfish
    lanternfish_counter[8] = new_lanternfish

print(sum(lanternfish_counter.values()))
