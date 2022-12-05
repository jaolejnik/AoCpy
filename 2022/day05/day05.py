import pathlib
import re
import copy

WORKDIR = str(pathlib.Path(__file__).parent.resolve())

# ----------- PART 1 -------------------
reading_stacks = True 
initialized_stacks = False 

stacks = [] 
instructions = []

with open(WORKDIR + "/input") as f:
    for line in f:
        if (not initialized_stacks):
            stacks = [[] for x in range(len(line) // 4)]
            initialized_stacks = True

        line = line.rstrip("\n")

        # I'm sure there's better way by using regex
        if (reading_stacks):
            stack_index = 0
            for i in range(1,len(line), 4):
                crate_id = line[i].strip()
                if crate_id and not crate_id.isdigit(): 
                    stacks[stack_index].insert(0, crate_id)
                stack_index += 1

            if(not line):
                reading_stacks = False
                continue

        else:
            instructions.append(tuple(map(int,re.findall(r'\d+', line))))


def move_crates_9000(amount, from_stack, to_stack):
    from_stack -= 1
    to_stack -= 1

    for i in range(amount):
        stacks[to_stack].append(stacks[from_stack].pop())

stacks_org = copy.deepcopy(stacks) 
for x in instructions:
    move_crates_9000(*x)

print("Part 1:", end="")
for stack in stacks:
    print(stack[-1], end="")
print()

# ----------- PART 2 -------------------
def move_crates_9001(amount, from_stack, to_stack):
    from_stack -= 1
    to_stack -= 1

    crates_to_move = [stacks[from_stack].pop() for i in range(amount)]
    crates_to_move.reverse()
    stacks[to_stack] = stacks[to_stack] + crates_to_move

stacks = stacks_org[:]
for x in instructions:
    move_crates_9001(*x)

print("Part 2:", end="")
for stack in stacks:
    print(stack[-1], end="")
print()

