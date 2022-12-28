import sys 


def part1(instructions):
    values = [1]
    for x in instructions:
        values.append(0)
        if x[0]=='addx':
            values.append(x[1])

    print(sum(values[:20])*20 + sum(values[:60])*60 + sum(values[:100])*100 + sum(values[:140])*140 + sum(values[:180])*180 + sum(values[:220])*220)
    
    return values

def part2(values):
    stripe, crt = '###' + '.'*37 , ''
    value = 1
    render = []
    for i in range(0,len(values)):
        if i%40==0:
            if i!=0:
                render.append(crt)
            crt = ''
        crt += stripe[i%40]
        value += values[i]
        stripe = '.'*40
        stripe = stripe[:value-1] + '###' + stripe[value+2:]
    render.append(crt)
    
    for x in render:
        print(x)
        

if __name__ == '__main__':
    input_list = open(sys.argv[1], "r").read().split("\n")
    instructions = [[x.split()[0], int(x.split()[1]) if len(x.split())>1 else 0] for x in input_list]
    values = part1(instructions)
    part2(values[1:])
