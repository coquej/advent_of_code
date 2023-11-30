import sys 
from math import lcm


def clean_list(input_list):
    new_list = []
    curr_monkey=[]
    for i in input_list:
        if i.__contains__('Monkey'):
            new_list.append(curr_monkey)
            curr_monkey=[]
        elif i.strip()!='':
            curr_monkey.append(i.strip())
    
    new_list.append(curr_monkey)
    

    for i in range(1,len(new_list)):
        new_list[i][0] = [int(x) for x in new_list[i][0].replace('Starting items: ', '').split(', ')]
        new_list[i][1] = new_list[i][1].replace('Operation: new = old ','')
        new_list[i][2] = int(new_list[i][2].replace('Test: divisible by ',''))
        new_list[i][3] = int(new_list[i][3].replace('If true: throw to monkey ',''))
        new_list[i][4] = int(new_list[i][4].replace('If false: throw to monkey ',''))

    return new_list[1:] # drop first empty list

def apply_operation(val, op):
    val2 = op.split(' ')[1]
    val2 = int(val2) if val2!='old' else val

    if op.startswith('*'):
        return val * val2
    else:
        return val + val2
    
def get_monkey_business(monkeys, worry_default, rounds=20):
    inspected = [0 for _ in range(len(monkeys))]
    div = lcm(*(monkey[2] for monkey in monkeys))


    for _ in range(rounds):
        for i in range(len(monkeys)):
            for j in range(len(monkeys[i][0])):
                inspected[i]+=1
                new = apply_operation(monkeys[i][0][j], monkeys[i][1])
                new = new%div if not worry_default else new//3
                if new%monkeys[i][2]==0:
                    monkeys[monkeys[i][3]][0] += [new] 
                else:
                    monkeys[monkeys[i][4]][0] += [new] 
            monkeys[i][0]=[]
        print(inspected)

    inspected.sort()
    return inspected[-1] * inspected[-2]


if __name__ == '__main__':
    input_list = open(sys.argv[1], "r").read().split("\n")
    cleaned_list = clean_list(input_list)

    print(get_monkey_business(cleaned_list,True,20))
    print(get_monkey_business(cleaned_list,False,1))