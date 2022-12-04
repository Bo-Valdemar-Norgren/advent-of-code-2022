from aocd.models import Puzzle

# Parse input
puzzle = Puzzle(2022, 4)
lines = puzzle.input_data.split("\n")

# Part 1
contains = 0
for line in lines:
    range1, range2 = line.split(",")
    x1, x2 = map(int, range1.split("-"))
    y1, y2 = map(int, range2.split("-"))

    if x1 <= y1 and x2 >= y2:
        contains += 1
    elif y1 <= x1 and y2 >= x2:
        contains += 1

puzzle.answer_a = contains

# Part 2
overlaps = 0
for line in lines:
    range1, range2 = line.split(",")
    x1, x2 = map(int, range1.split("-"))
    y1, y2 = map(int, range2.split("-"))

    if x1 <= y1 and x2 >= y1:
        overlaps += 1
    elif y1 <= x1 and y2 >= x1:
        overlaps += 1

puzzle.answer_b = overlaps
