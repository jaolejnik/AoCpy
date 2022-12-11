import pathlib
import copy
import math

WORKDIR = str(pathlib.Path(__file__).parent.resolve())


class Monkey:
    def __init__(self, raw_data):
        self.id = int(raw_data[0].split()[1].rstrip(":"))
        self.items = list(map(int, raw_data[1].split(":")[1].split(",")))
        self.operation = raw_data[2].split("=")[1].strip()
        self.test = int(raw_data[3].split()[-1])
        self.target = (
            int(raw_data[5].split()[-1]),  # test == False
            int(raw_data[4].split()[-1]),  # test == True
        )
        self.inspected_items = 0

    def inspect_item(self, lcm):
        self.inspected_items += 1

        old = self.items.pop(0)  # old worry level
        new_worry_level = eval(self.operation)
        if lcm:
            new_worry_level = new_worry_level % lcm
        else:
            new_worry_level = new_worry_level // 3
        is_divisible = new_worry_level % self.test == 0
        new_monkey_id = self.target[int(is_divisible)]

        return new_monkey_id, new_worry_level

    def receive_item(self, item):
        self.items.append(item)

    def has_item(self):
        return len(self.items) > 0

    def __str__(self):
        return "\n".join(
            [
                "----------------------------------------",
                f"Monkey {self.id}:",
                f"  Inspected items: {self.inspected_items}",
                f"  Items: {self.items}",
                f"  Operation: new = {self.operation}",
                f"  Test: divisible by {self.test}",
                f"    True: throw to {self.target[1]}",
                f"    False: throw to {self.target[0]}",
            ]
        )


# ----------- PART 1 -------------------
monkeys = []

with open(WORKDIR + "/input") as f:
    monkey_data = []
    for i, line in enumerate(f, 1):
        if line == "\n":
            continue
        monkey_data.append(line.strip())
        if i % 7 == 6:
            monkeys.append(Monkey(monkey_data))
            monkey_data = []


def get_monkey_business(monkeys, rounds, lcm=None):
    for i in range(rounds):
        resolve_round(monkeys, lcm)

    monkey_business = [monkey.inspected_items for monkey in monkeys]
    monkey_business.sort(reverse=True)
    return monkey_business[0] * monkey_business[1]


def resolve_round(monkeys, lcm):
    for i in range(len(monkeys)):
        resolve_turn(monkeys, i, lcm)


def resolve_turn(monkeys, monkey_id, lcm):
    current_monkey = monkeys[monkey_id]
    while current_monkey.has_item():
        new_monkey_id, item_worry_level = current_monkey.inspect_item(lcm)
        monkeys[new_monkey_id].receive_item(item_worry_level)


print("Part 1:", get_monkey_business(copy.deepcopy(monkeys), 20))


# ----------- PART 2 -------------------
# CONFESSION: I knew there's gotta be something with modulo and LCM
# but wasn't sure what values exactly and had to get a hint
monkey_test_lcm = math.lcm(*[monkey.test for monkey in monkeys])
print("Part 2:", get_monkey_business(monkeys, 10000, monkey_test_lcm))
