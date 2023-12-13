import sys
import numpy as np

def clean_input_part1(file):
    lines = open(file, "r").read().split("\n")

    time = [int(x) for x in lines[0].split(":")[1].split()]
    distance = [int(x) for x in lines[1].split(":")[1].split()]

    return time, distance

def clean_input_part2(file):
    lines = open(file, "r").read().split("\n")

    time = int(lines[0].split(":")[1].replace(' ',''))
    distance = int(lines[1].split(":")[1].replace(' ',''))

    return time, distance

def calculate_score(time, distance, part='part1'):
    possibilities = [0]*len(distance) if part=='part1' else [0]

    if part=='part1':
        for race in range(0, len(time)):
            for min in range(0, time[race]):
                possibilities[race] += 1 if min*(time[race]-min)>distance[race] else 0
    else:
        for min in range(0, time):
            possibilities[0] += 1 if min*(time-min)>distance else 0

    return np.prod(possibilities)

if __name__ == "__main__":
    time1, distance1 = clean_input_part1(sys.argv[1])
    time2, distance2 = clean_input_part2(sys.argv[1])

    print(calculate_score(time1, distance1))
    print(calculate_score(time2, distance2, 'part2'))