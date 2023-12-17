import sys
from math import gcd

def clean_input(file):
    lines = open(file, "r").read().split("\n")
    instructions = [0 if x=='L' else 1 for x in lines[0]]
    tree = {}

    for line in lines[2:]:
        parent, children = line.split(' = ')
        left, right = children[1:-1].split(', ')
        tree[parent] = (left, right)

    return instructions, tree

def part1(instructions, tree):
    curr = 'AAA'
    instr_i = 0
    steps = 0

    while curr!='ZZZ':
        curr = tree[curr][instructions[instr_i]]
        instr_i = 0 if instr_i==len(instructions)-1 else instr_i+1
        steps += 1

    return steps

def lcm(steps):
    x = 1
    for i in steps:
         x = x*i//gcd(x, i)
    return x
    
def part2(instructions, tree):
    curr_nodes = [x for x in tree.keys() if x[-1]=='A']
    instr_i = 0
    steps = 1
    steps_per_node = []

    while len(curr_nodes)!=0:
        new_curr_nodes = []
        for curr in curr_nodes: 
            new_node = tree[curr][instructions[instr_i]]
            if tree[curr][instructions[instr_i]][-1]=='Z':
                steps_per_node.append(steps)
            else:
                new_curr_nodes.append(new_node)
        curr_nodes = new_curr_nodes
        instr_i = 0 if instr_i==len(instructions)-1 else instr_i+1
        steps += 1

    return lcm(steps_per_node)

if __name__ == "__main__":
    instructions, tree = clean_input(sys.argv[1])

    if len(sys.argv)==3:
        if sys.argv[2]=='part1':    
            print('Part 1 solution:', part1(instructions, tree))
        else:
            print('Part 2 solution:', part2(instructions, tree))
    else:
        print('Part 1 solution:', part1(instructions, tree))
        print('Part 2 solution:', part2(instructions, tree))

