from aocd.models import Puzzle

# Parse input
puzzle = Puzzle(2022, 5)
lines = puzzle.input_data.split("\n")

# Variables
stack_range = range(1, len(lines[0]), 4)
stacks = [[] for _ in stack_range]
move_commands = []

# Extract stack descriptions and move commands from input
for line in lines:
    stripped = line.lstrip()
    # Stack description
    if stripped.startswith("["):
        for stack_i, char_i in enumerate(stack_range):
            if line[char_i] != ' ':
                stacks[stack_i].append(line[char_i])
    # Move command
    elif stripped.startswith("move"):
        separated = line.split()
        move_commands.append((int(separated[1]), int(separated[3]) - 1, int(separated[5]) - 1))

# Invert the stacks so top is back of the list
for stack in stacks:
    stack.reverse()

# Execute move commands
for command in move_commands:
    n, s_index_1, s_index_2 = command
    last_n_elems = stacks[s_index_1][-n:]
    last_n_elems.reverse() # Comment this line for part 2 solution
    stacks[s_index_2] += last_n_elems
    del stacks[s_index_1][-n:]

answer = "".join([stack[len(stack) - 1] for stack in stacks if stack])
puzzle.answer_a = answer
puzzle.answer_b = answer
