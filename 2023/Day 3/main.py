import sys


def pos_symbol_adj(lines, i, j, specific):
    # this returns position of symbol if any symbol (specified or not) is adjacent

    if lines[i][j].isnumeric():
        for x in [-1, 0, +1]:
            for y in [-1, 0, +1]:
                if ((i+x)<=len(lines)-1 and (i+x)>0) and (j+y)<=len(lines[i])-1 and (j+y)>0: # if is in between matrix scope
                        if (not (x==0 and y==0)) and (not lines[x+i][y+j].isalnum() and lines[x+i][y+j]!='.'): # if is not current position and is a symbol
                            if (specific=='*' and lines[x+i][y+j]=='*') or specific=='':
                                return (x+i,y+j)
    return None
                            
def identify_adjacents(lines, check=''):
    # this returns a dict with pairs like: 
    # adjacents_dic = {pos_symbol_1 : [pos_adjacent_to_symbol_1_1, pos_adjacent_to_symbol_1_2, ...]}

    adjacents_dic = {} 
    
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            pos_symbol = pos_symbol_adj(lines, i, j, specific=check)
            if pos_symbol is not None:
                adjacents_dic[pos_symbol] = [(i,j)] if pos_symbol not in adjacents_dic.keys() else adjacents_dic[pos_symbol]+[(i,j)]

    return adjacents_dic

def identify_numbers(lines):
    # this returns a list of numbers in input like : 
    #  numbers_list = [["number1",["positions of chars that contain the number1"]], ["number2",["positions of chars that contain the number2"]], ...]

    current_number_pos = ['',[]]
    numbers_list = []

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j].isnumeric():
                current_number_pos[0]+=lines[i][j]
                current_number_pos[1].append((i,j))
            elif len(current_number_pos[0])>0:
                numbers_list.append(current_number_pos)
                current_number_pos = ['',[]]

    return numbers_list

def part1(lines):
    adjacent_positions = identify_adjacents(lines)
    number_positions = identify_numbers(lines)
    numers_to_sum = []

    adjacents = set([adj for adjacents in adjacent_positions.values() for adj in adjacents])

    for number in number_positions:
        for adjacent in list(adjacents):
            if adjacent in number[1]:
                numers_to_sum.append(int(number[0]))
                break
    
    return sum(numers_to_sum)

def part2(lines):
    adjacent_positions = identify_adjacents(lines, check='*')
    number_positions = identify_numbers(lines)
    res = 0

    for _, adjacent_positions in adjacent_positions.items():
        nums_to_mult = []
        for number in number_positions:
            for adj_position in adjacent_positions:
                if adj_position in number[1]:
                    nums_to_mult.append(int(number[0]))
                    break
        if len(nums_to_mult)==2:
            res+=(nums_to_mult[0]*nums_to_mult[1])

    return res


if __name__ == "__main__":
    file = sys.argv[1]
    lines = open(file, "r").read().split("\n")

    print('Part 1:', part1(lines))
    print('Part 2:', part2(lines))
