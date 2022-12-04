import pathlib

WORKDIR = str(pathlib.Path(__file__).parent.resolve())

# ----------- PART 1 -------------------
elf_pairs = []
with open(WORKDIR + "/input") as f:
    for line in f:
        elf_a, elf_b = line.strip().split(",")
        a = tuple(map(int, elf_a.split("-")))
        b = tuple(map(int, elf_b.split("-")))

        elf_pairs.append((a, b))


def check_for_complete_overlap(a, b):
    if a[1] - a[0] < b[1] - b[0]:
        return a[0] >= b[0] and a[1] <= b[1]
    else:
        return b[0] >= a[0] and b[1] <= a[1]


complete_overlap_count = sum(
    [check_for_complete_overlap(*range_pair) for range_pair in elf_pairs]
)

print("Part 1:", complete_overlap_count)

# ----------- PART 2 -------------------
def check_for_any_overlap(a, b):
    if a[1] - a[0] < b[1] - b[0]:
        return b[0] <= a[0] <= b[1] or b[0] <= a[1] <= b[1]
    else:
        return a[0] <= b[0] <= a[1] or a[0] <= b[1] <= a[1]


any_overlap_count = sum(
    [check_for_any_overlap(*range_pair) for range_pair in elf_pairs]
)

print("Part 2:", any_overlap_count)
