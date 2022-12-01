from aocd.models import Puzzle
from collections import defaultdict

# Parse input
puzzle = Puzzle(2022, 1)
lines = puzzle.input_data.split("\n")

elf_dict = defaultdict(int)
i = 0
for line in lines:
    if not line == '':
        elf_dict[i] += int(line)
    else:
        i += 1

puzzle.answer_a = max(elf_dict.values())
puzzle.answer_b = sum(sorted(elf_dict.values(), reverse=True)[:3])
