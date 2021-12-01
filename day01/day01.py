import pathlib

WORKDIR = str(pathlib.Path(__file__).parent.resolve())

# ----------- PART 1 -------------------
increase_counter = 0
prev_value = None

with open(WORKDIR + "/input") as f:
    for line in f:
        value = int(line.strip())
        if prev_value is not None:
            increase_counter += value - prev_value > 0
        prev_value = value

print(increase_counter)

# ----------- PART 2 -------------------
increase_counter = 0
measure_groups = []
data = {}

with open(WORKDIR + "/input") as f:
    for i, line in enumerate(f, 1):
        measure_groups.append(i)
        for group in measure_groups:
            if group not in data:
                data[group] = 0
            data[group] += int(line.strip())
        if len(measure_groups) == 3:
            del measure_groups[0]

for i in range(1, len(data.keys())):
    key1 = list(data.keys())[i]
    key2 = list(data.keys())[i - 1]
    increase_counter += data[key1] - data[key2] > 0

print(increase_counter)
