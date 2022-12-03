from aocd.models import Puzzle

# Parse input
puzzle = Puzzle(2022, 3)
lines = puzzle.input_data.split("\n")
compartments = [(line[:len(line) // 2], line[len(line) // 2:]) for line in lines]

lower_case = "".join([chr(i) for i in range(ord('a'), ord('z') + 1)])
all_letters = lower_case + lower_case.upper()

# Part 1
score_a = 0
for comp in compartments:
    (common_c, ) = set(comp[0]).intersection(comp[1])
    score_a += all_letters.index(common_c) + 1
puzzle.answer_a = score_a

# Part 2
score_b = 0
for i in range(0, len(lines) - 1, 3):
    (common_c, ) = set(lines[i]).intersection(lines[i + 1]).intersection(lines[i + 2])
    score_b += all_letters.index(common_c) + 1
puzzle.answer_b = score_b
