import sys

def clean_input(file):
    lines = open(file, "r").read().split("\n")

    return [[int(x) for x in line.split(' ')] for line in lines]

def get_sequence_history(line):
    series = [line]
    while sum([0!=x for x in series[-1]])!=0:
        curr_serie = series[-1]
        new_serie = []
        for i in range(len(curr_serie)-1):
            new_serie.append(curr_serie[i+1]-curr_serie[i])
        series.append(new_serie)    
    return series

def part1(lines):
    res = []

    for line in lines:
        series = get_sequence_history(line)
        curr = 0
        for i in range(1, len(series)):
            curr = series[len(series)-1-i][-1]+curr
        res.append(curr)

    return sum(res)

def part2(lines):
    res = []

    for line in lines:
        series = get_sequence_history(line)
        curr = 0
        for i in range(1, len(series)):
            curr = series[len(series)-1-i][0]-curr
        res.append(curr)

    return sum(res)


if __name__ == "__main__":
    lines = clean_input(sys.argv[1])

    print(part1(lines))
    print(part2(lines))
