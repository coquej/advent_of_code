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

expanded_tiles = {
    '|' : [[' ', '*', ' '],[' ', '*', ' '],[' ', '*', ' ']],
    '-' : [[' ', ' ', ' '],['*', '*', '*'],[' ', ' ', ' ']],
    'L' : [[' ', '*', ' '],[' ', '*', '*'],[' ', ' ', ' ']],
    'J' : [[' ', '*', ' '],['*', '*', ' '],[' ', ' ', ' ']],
    '7' : [[' ', ' ', ' '],['*', '*', ' '],[' ', '*', ' ']],
    'F' : [[' ', ' ', ' '],[' ', '*', '*'],[' ', '*', ' ']],
    '.' : [[' ', ' ', ' '],[' ', ' ', ' '],[' ', ' ', ' ']],
    'S' : [['*', '*', '*'],['*', '*', '*'],['*', '*', '*']]
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

    return steps, visited

def expand_map(lines):
    res = [[expanded_tiles[x] for x in line] for line in lines]

    return [(list(''.join([''.join(x[i]) for x in line]))) for line in res for i in [0,1,2]]

def fill_neighbors(matrix, a, b, visited, to_visit):
    i, j = a, b
    to_visit.add((i, j))

    while len(to_visit)!=0:
        (i, j) = to_visit.pop()
        visited.add((i, j))

        if 0 <= i < len(matrix) and 0 <= j < len(matrix[i]) and matrix[i][j] == ' ':
            matrix[i][j] = 'W'
            if i+1 < len(matrix) and (i+1, j) not in visited:
                to_visit.add((i+1, j))
            if i-1 >= 0 and (i-1, j) not in visited:
                to_visit.add((i-1, j))
            if j+1 < len(matrix[0]) and (i, j+1) not in visited:
                to_visit.add((i, j+1))
            if j-1 < len(matrix[0]) and (i, j-1) not in visited:
                to_visit.add((i, j-1))

def is_fully_empty(i, j, draw):
    for k in [i-1, i, i+1]:
        for l in [j-1, j, j+1]:
            if draw[k][l] != ' ':
                return False
    
    return True

def part2(lines, visited):
    # Removing not path elements
    cleaned_lines = [''.join([lines[i][j] if (i,j) in visited else '.' for j in range(len(lines[i]))]) for i in range(len(lines))]

    # Expand map to 3x3 cells
    draw = expand_map(cleaned_lines)

    # Draw 'W' with neighbours from the first and last columns and rows, until reaching the loop "walls"
    visited = set()
    to_visit = set()
    for i in [0, len(draw) - 1]:
        for j in range(len(draw[i])):
            if draw[i][j] == ' ':
                fill_neighbors(draw, i, j, visited, to_visit)

    for i in range(len(draw)):
        for j in [0, len(draw[i]) - 1]:
            if draw[i][j] == ' ':
                fill_neighbors(draw, i, j, visited, to_visit)
    
    # Count as "Full Empty" cell if all 3x3 cells (previously expanded) were not filled with W or other symbols than ' '.
    inner_tiles = sum([1 if is_fully_empty(i, j, draw) else 0 for i in range(len(draw)) for j in range(len(draw[i]))])

    # Divide by 9 to get results after reducing the 3x3 cells
    return int(inner_tiles/9)


if __name__ == "__main__":
    lines = clean_input(sys.argv[1])

    res1, visited = part1(lines)
    print('Part 1:', res1)
    print('Part 2:', part2(lines, visited))
