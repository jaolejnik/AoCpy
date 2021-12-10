import pathlib
from statistics import median

WORKDIR = str(pathlib.Path(__file__).parent.resolve())

opening = ("(", "[", "{", "<")
closing = (")", "]", "}", ">")

pair = {k: v for k, v in zip(opening, closing)}

with open(WORKDIR + "/input") as f:
    data = [line.strip() for line in f]

# ----------- PART 1 -------------------
points_map = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}


def find_mismatched_bracket(line):
    opened = []
    for bracket in line:
        if not opened or bracket in opening:
            opened.append(bracket)
            continue
        if opened[-1] in opening and bracket in closing and pair[opened[-1]] == bracket:
            opened.pop()
            continue
        else:
            return bracket


def remove_corrupted_lines(data):
    new_data = []
    score = 0
    for line in data:
        points = points_map.get(find_mismatched_bracket(line), 0)
        score += points
        if points == 0:
            new_data.append(line)

    return new_data, score


data, score = remove_corrupted_lines(data)
print(score)

# ----------- PART 2 -------------------
points_map = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


def find_missing_brackets(line):
    opened = []
    for bracket in line:
        if not opened or bracket in opening:
            opened.append(bracket)
            continue
        if opened[-1] in opening and bracket in closing and pair[opened[-1]] == bracket:
            opened.pop()
            continue

    return opened


def score_completion_string(completion_string):
    score = 0
    for bracket in completion_string:
        score *= 5
        score += points_map[bracket]

    return score


def calculate_scores(data):
    scores = []
    for line in data:
        missing_brackets = find_missing_brackets(line)
        missing_brackets.reverse()
        completion_string = [pair[bracket] for bracket in missing_brackets]
        scores.append(score_completion_string(completion_string))

    return scores


scores = calculate_scores(data)
scores.sort()
print(median(scores))
