from aocd.models import Puzzle
from collections import defaultdict

# Parse input
puzzle = Puzzle(2022, 2)
lines = puzzle.input_data.split("\n")

scoring = defaultdict(int,
    {
    "A Y" : 6,
    "B Z" : 6,
    "C X" : 6,
    "A X" : 3,
    "B Y" : 3,
    "C Z" : 3,
    "X"   : 1,
    "Y"   : 2,
    "Z"   : 3
    }
)

strategy = {
    "A X" : "A Z", # loss
    "A Y" : "A X", # draw
    "A Z" : "A Y", # win
    "B X" : "B X", # loss
    "B Y" : "B Y", # draw
    "B Z" : "B Z", # win
    "C X" : "C Y", # loss
    "C Y" : "C Z", # draw
    "C Z" : "C X"  # win
}

puzzle.answer_a = sum([scoring[line] + scoring[line[2]] for line in lines])
puzzle.answer_b = sum([scoring[strategy[line]] + scoring[strategy[line][2]] for line in lines])
