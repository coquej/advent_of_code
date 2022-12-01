import sys 

def clean(input_list):
    cleaned_list, sublist = [], []
    for x in input_list:
        if x=='':
            cleaned_list.append(sublist)
            sublist = []
        else:
            sublist.append(int(x))
    
    if sublist != []:
        cleaned_list.append(sublist)

    return cleaned_list

def part1(input_list):
    calories = [sum(x) for x in input_list]
    print("Part 1 solution: ", max(calories))


def part2(input_list):
    calories = [sum(x) for x in input_list]
    calories.sort()
    print("Part 2 solution: ", sum(calories[-3:]))


if __name__ == '__main__':
    input_list = open(sys.argv[1], "r").read().split("\n")

    cleaned_list = clean(input_list)

    part1(cleaned_list)
    part2(cleaned_list)