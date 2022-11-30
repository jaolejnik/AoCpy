import pathlib

WORKDIR = str(pathlib.Path(__file__).parent.resolve())

# ----------- PART 1 -------------------
easy_digits = {2: 1, 4: 4, 3: 7, 7: 8}

counter = 0
with open(WORKDIR + "/input") as f:
    for line in f:
        outputs = line.split("|")[1].strip().split(" ")
        for pattern in outputs:
            counter += len(pattern) in easy_digits.keys()

print(counter)
# ----------- PART 2 -------------------
# It's a mess, I know...
# But it's a mess that works!
def find_mapping(coded_digits, digit_to_pattern):
    pattern_to_digit = {v: str(k) for k, v in digit_to_pattern.items()}

    def is_3(pattern):
        return (
            digit_to_pattern["1"][0] in pattern and digit_to_pattern["1"][1] in pattern
        )

    def is_9(pattern):
        for char in digit_to_pattern["4"]:
            if char not in pattern:
                return False
        return True

    def is_2(pattern):
        for char in pattern:
            if char not in digit_to_pattern["9"]:
                return True
        return False

    while len(pattern_to_digit) != 10:
        for pattern in coded_digits:
            if pattern in pattern_to_digit.keys():
                continue

            if len(pattern) == 5:
                if "2" in pattern_to_digit.values():
                    pattern_to_digit[pattern] = "5"
                    digit_to_pattern["5"] = pattern

                if is_3(pattern):
                    pattern_to_digit[pattern] = "3"
                    digit_to_pattern["3"] = pattern

                if "9" in pattern_to_digit.values():
                    if is_2(pattern):
                        pattern_to_digit[pattern] = "2"
                        digit_to_pattern["2"] = pattern

            if len(pattern) == 6:
                if set(["6", "9"]) <= set(pattern_to_digit.values()):
                    pattern_to_digit[pattern] = "0"
                    digit_to_pattern["0"] = pattern

                if is_9(pattern):
                    pattern_to_digit[pattern] = "9"
                    digit_to_pattern["9"] = pattern

                if "9" in pattern_to_digit.values():
                    for char in digit_to_pattern["8"]:
                        if char not in pattern and char in digit_to_pattern["1"]:
                            pattern_to_digit[pattern] = "6"
                            digit_to_pattern["6"] = pattern

    return pattern_to_digit


total_sum = 0
with open(WORKDIR + "/input") as f:
    for line in f:
        coded_digits, outputs = [
            string.strip().split(" ") for string in line.split("|")
        ]
        digit_to_pattern = {}
        for pattern in coded_digits:
            if len(pattern) in easy_digits.keys():
                digit_to_pattern[str(easy_digits[len(pattern)])] = pattern
        pattern_to_digit = find_mapping(coded_digits, digit_to_pattern)
        sorted_pattern_map = {
            "".join(sorted(k)): v for k, v in pattern_to_digit.items()
        }
        total_sum += int(
            "".join(
                [sorted_pattern_map["".join(sorted(pattern))] for pattern in outputs]
            )
        )

print(total_sum)
