import pathlib

WORKDIR = str(pathlib.Path(__file__).parent.resolve())

# ----------- PART 1 -------------------
elves_calories = [0]

with open(WORKDIR + "/input") as f:
    for line in f:
        if line == "\n":
            elves_calories.append(0)
            continue
        elves_calories[-1] += int(line.strip())

print("Part 1:", max(elves_calories))

# ----------- PART 2 -------------------
elves_calories.sort(reverse=True)
print("Part 2:", sum(elves_calories[:3]))
