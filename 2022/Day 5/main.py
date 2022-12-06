import sys 


def clean_instr(instr):
    return [[int(x) for x in line.split(' ') if not x.isalpha()] for line in instr]

def clean_stacks(st):
    n_stacks = int(st[-1].strip()[-1])
    stacks = [[] for _ in range(n_stacks)]
    for line in st:
        for i in range(n_stacks):
            to_append = line[1+3*i+i]
            if to_append.isalpha():
                stacks[i].append(to_append)
    return stacks

def solution(stacks, instr, part):
    res = stacks.copy()
    for i in instr:
        moved = res[i[1]-1][:i[0]].copy()
        if part==1: moved.reverse()
        res[i[1]-1] = res[i[1]-1][i[0]:].copy()
        res[i[2]-1]  = moved + res[i[2]-1]
    
    print("Part", part, "solution: ", ''.join([x[0] for x in res]))

if __name__ == '__main__':
    input_list = open(sys.argv[1], "r").read().split("\n\n")

    instr = input_list[1].split("\n")
    instr = clean_instr(instr)

    stacks = input_list[0].split("\n")
    stacks = clean_stacks(stacks)

    solution(stacks, instr, 1)
    solution(stacks, instr, 2)

