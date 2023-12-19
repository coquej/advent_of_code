import sys

pipes = { # movements [DOWN, UP, LEFT, RIGHT]
    '|' : [1, 1, 0, 0],
    '-' : [0, 0, 1, 1],
    'L' : [0, 1, 0, 1],
    'J' : [0, 1, 1, 0],
    '7' : [1, 0, 1, 0],
    'F' : [1, 0, 0, 1],
    '.' : [0, 0, 0, 0],
    'S' : [1, 1, 1, 1]
}


def clean_input(file):
    return open(file, "r").read().split("\n")

def find_s(lines):
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j]=='S':
                return i, j

def get_new_pipes(symbol, i, j, lines):
    moves = [(a * x, b * x) for (a, b), x in zip([(1, 0), (-1, 0), (0, -1), (0, 1)], pipes[symbol])]
    new_pos = []

    for x in range(len(moves)):
        new_i, new_j = i + moves[x][0], j + moves[x][1]
        
        # As new pipe should have connections the other way around with the previous pipe, we reverse x
        x_new_pos = x+1 if x%2 == 0 else x-1
        
        if new_i >= 0 and new_i<len(lines): # NORTH/SOUTH bounds
            if new_j >= 0 and new_j<len(lines[new_i]): # EAST/WEST bounds
                if pipes[lines[new_i][new_j]][x_new_pos]: # Movement can be done
                    new_pos.append((new_i, new_j))

    return new_pos

def part1(lines):
    i, j = find_s(lines)
    curr_pos = get_new_pipes('S', i, j, lines)
    visited = {(i, j)}
    steps = 0
    while len(curr_pos) > 0:
        next_pos = []
        for i, j in list(curr_pos):
            visited.add((i, j))
            next_pos += get_new_pipes(lines[i][j], i, j, lines)
        steps += 1
        curr_pos = set(next_pos) - visited

    return steps

if __name__ == "__main__":
    lines = clean_input(sys.argv[1])
    print('Part 1:', part1(lines))
