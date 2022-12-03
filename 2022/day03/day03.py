import pathlib
from dataclasses import dataclass

WORKDIR = str(pathlib.Path(__file__).parent.resolve())


# ----------- PART 1 -------------------
lowercase_priority = {chr(i + 97): i + 1 for i in range(26)}
uppercase_priority = {chr(i + 65): i + 27 for i in range(26)}
item_to_priority = {**lowercase_priority, **uppercase_priority}

rucksacks = []

with open(WORKDIR + "/input") as f:
    for line in f:
        rucksacks.append(line.strip())


def divide_into_compartments(rucksack):
    comp_size = len(rucksack) // 2

    return (
        set(rucksack[:comp_size]),
        set(rucksack[comp_size:]),
    )


def calculate_priority(rucksack):
    comp_a, comp_b = divide_into_compartments(rucksack)
    comp_overlap = comp_a.intersection(comp_b)
    common_item = next(iter(comp_overlap))

    return item_to_priority[common_item]


priority_sum = sum([calculate_priority(r) for r in rucksacks])
print("Part 1:", priority_sum)

# ----------- PART 2 -------------------
def calculate_group_priority(group_rucksacks):
    r_overlap = set(group_rucksacks.pop(0))
    for r in group_rucksacks:
        r_overlap = r_overlap.intersection(set(r))

    common_item = next(iter(r_overlap))

    return item_to_priority[common_item]


group_priority_sum = sum(
    [
        calculate_group_priority(rucksacks[i : i + 3])
        for i in range(0, len(rucksacks), 3)
    ]
)

print("Part 2:", group_priority_sum)
