from aocd.models import Puzzle

# Parse input
puzzle = Puzzle(2022, 6)
lines = puzzle.input_data.split("\n")

data_string = lines[0]

def find_marker(data_string, distinct_chars):
    character_window = list(data_string[:distinct_chars])
    if len(set(character_window)) == distinct_chars:
        return distinct_chars

    for i in range(distinct_chars, len(data_string)):
        character_window[i % distinct_chars] = data_string[i]

        if len(set(character_window)) == distinct_chars:
            return i + 1
    
    return None

puzzle.answer_a = find_marker(data_string, 4)
puzzle.answer_b = find_marker(data_string, 14)
