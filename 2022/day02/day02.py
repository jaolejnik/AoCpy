import pathlib

WORKDIR = str(pathlib.Path(__file__).parent.resolve())


ROCK = 1
PAPER = 2
SCISSORS = 3

# DIRTY QUICK SOLUTION BY SLEEPY ME
# ------------------------------------------------------------
print("DIRTY QUICK")
# ----------- PART 1 -------------------
def calculate_points(opponent, you):
    if opponent == "A":
        if you == "X":
            return 3 + ROCK
        if you == "Y":
            return 6 + PAPER
        if you == "Z":
            return 0 + SCISSORS

    elif opponent == "B":
        if you == "X":
            return 0 + ROCK
        if you == "Y":
            return 3 + PAPER
        if you == "Z":
            return 6 + SCISSORS

    elif opponent == "C":
        if you == "X":
            return 6 + ROCK
        if you == "Y":
            return 0 + PAPER
        if you == "Z":
            return 3 + SCISSORS


guide_data = []

with open(WORKDIR + "/input") as f:
    for line in f:
        guide_data.append(line.strip().upper().split())

total_score = sum([calculate_points(*data) for data in guide_data])
print("Part 1:", total_score)

# ----------- PART 2 -------------------
def calculate_points2(opponent, condition):
    if condition == "X":
        points = 0
        if opponent == "A":
            points += SCISSORS
        if opponent == "B":
            points += ROCK
        if opponent == "C":
            points += PAPER

    elif condition == "Y":
        points = 3
        if opponent == "A":
            points += ROCK
        if opponent == "B":
            points += PAPER
        if opponent == "C":
            points += SCISSORS

    elif condition == "Z":
        points = 6
        if opponent == "A":
            points += PAPER
        if opponent == "B":
            points += SCISSORS
        if opponent == "C":
            points += ROCK

    return points


total_score = sum([calculate_points2(*data) for data in guide_data])
print("Part 2:", total_score)

# A CLEANER SOLUTION AFTER I HAD SOME BREAKFEST AND COFEE
# ------------------------------------------------------------

print("CLEAN SLOW")

# ----------- PART 1 -------------------
code_to_value = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3,
}


def calculate_points_clean(opponent_code, you_code):
    opponent = code_to_value[opponent_code]
    you = code_to_value[you_code]

    win_points = 0
    if opponent - you == 0:  # DRAW
        win_points = 3

    if opponent - you in [-1, 2]:  # WIN
        win_points = 6
    # else LOSE

    return you + win_points


total_score = sum([calculate_points_clean(*data) for data in guide_data])
print("Part 1:", total_score)


# ----------- PART 2 -------------------
condition_to_value = {
    "X": 0,
    "Y": 3,
    "Z": 6,
}


def calculate_points_clean2(opponent_code, condition):
    opponent = code_to_value[opponent_code]
    you = 0

    if condition == "X":  # LOSE
        you = (opponent - 2) % 3 + 1

    if condition == "Y":  # DRAW
        you = opponent

    if condition == "Z":  # WIN
        you = opponent % 3 + 1

    return you + condition_to_value[condition]


total_score = sum([calculate_points_clean2(*data) for data in guide_data])
print("Part 2:", total_score)
