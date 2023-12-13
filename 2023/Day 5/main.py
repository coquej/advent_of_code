import sys

def clean_input(file):
    lines = open(file, "r").read().split("\n")
    
    seeds = [int(x) for x in lines[0].split(':')[1].split(' ') if x !='']
    transitions = {}

    for line in lines[2:]:
        if line!='':
            if line.endswith('map:'):
                current_transition = line[:-5]
                transitions[current_transition] = None
            else:
                transitions[current_transition] = [[int(x) for x in line.split(' ')]] if transitions[current_transition] is None \
                                                                else transitions[current_transition]+[[int(x) for x in line.split(' ')]]
    
    return seeds, transitions

def part1(seeds, transitions):
    locations = []

    for seed in seeds:
        curr_pos = seed
        for _, value in transitions.items():
            for val in value:
                min_src, max_src, add_to_src = val[1], val[1]+val[2], val[0]-val[1]
                if curr_pos < max_src and curr_pos >= min_src:
                    curr_pos += add_to_src
                    break
        locations.append(min(curr_pos, sys.maxsize))

    return min(locations)


def part2(seeds, transitions):
    ranges = [ [seeds[i], seeds[i]+seeds[i+1]+1] for i in range(0, len(seeds), 2)]

    # each iteration in this loop will have positions updated in "ranges" list (iteration of transations and then positions, the other way around
    # compared to part1 approach)
    for _, value in transitions.items():
        i = 0
        while i<len(ranges):           
            for val in value:
                min_src, max_src, add_to_src = val[1], val[1]+val[2]-1, val[0]-val[1]
                if ranges[i][0] <= max_src and ranges[i][0] >= min_src:
                    ranges[i][0] += add_to_src
                    if ranges[i][1] <= max_src:
                        ranges[i][1] += add_to_src
                    else:
                        ranges.append([max_src+1, ranges[i][1]])
                        ranges[i][1] = max_src + add_to_src
                    break
            i += 1
    
    return min([x[0] for x in ranges])

if __name__ == "__main__":
    seeds, transitions = clean_input(sys.argv[1])
    
    print(part1(seeds, transitions))
    print(part2(seeds, transitions))