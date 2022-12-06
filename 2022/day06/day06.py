import pathlib

WORKDIR = str(pathlib.Path(__file__).parent.resolve())

# ----------- PART 1 -------------------
with open(WORKDIR + "/input_test") as f:
    data = f.readline().strip()

def find_marker(signal, marker_width):
    i = 0;
    while True:
        marker = data[i:i+marker_width]
        if len(set(marker)) == marker_width:
            return (i, i + marker_width), marker
        i += 1

indices, marker = find_marker(data, 4)
print("Part 1:", indices[1])

# ----------- PART 2 -------------------
indices, marker = find_marker(data, 14)
print("Part 1:", indices[1])
