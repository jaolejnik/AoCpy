import pathlib

WORKDIR = str(pathlib.Path(__file__).parent.resolve())

# ----------- PART 1 -------------------
string_len = 12
index_count = [[0, 0] for i in range(string_len)]
with open(WORKDIR + "/input") as f:
    for line in f:
        for i, char in enumerate(line.strip()):
            index_count[i][int(char)] += 1

gamma_list = []
for bits in index_count:
    max_count = max(bits)
    most_common = bits.index(max_count)
    gamma_list.append(str(most_common))

gamma = int("".join(gamma_list), 2)
epsilon_list = ["0" if x == "1" else "1" for x in gamma_list]
epsilon = int("".join(epsilon_list), 2)

print(gamma * epsilon)


# ----------- PART 2 -------------------
string_len = 12
generator = []
scrubber = []
with open(WORKDIR + "/input") as f:
    for line in f:
        generator.append(line.strip())
        scrubber.append(line.strip())

i = 0
while len(generator) > 1:
    index_count = [0, 0]
    for data in generator:
        index_count[int(data[i])] += 1
    if index_count[0] == index_count[1]:
        most_common = "1"
    else:
        max_count = max(index_count)
        most_common = str(index_count.index(max_count))
    generator = [x for x in generator if x[i] == most_common]
    i += 1

i = 0
while len(scrubber) > 1:
    index_count = [0, 0]
    for data in scrubber:
        index_count[int(data[i])] += 1
    if index_count[0] == index_count[1]:
        least_common = "0"
    else:
        min_count = min(index_count)
        least_common = str(index_count.index(min_count))
    scrubber = [x for x in scrubber if x[i] == least_common]
    i += 1

generator = int(generator[0], 2)
scrubber = int(scrubber[0], 2)

print(generator * scrubber)
