import sys 
import string


def clean_for_part1(input_list):
    res = [[x[:int(len(x)/2)], x[int(len(x)/2):]] for x in input_list]
    return res

def clean_for_part2(input_list):
    res = [input_list[i:i+3] for i in range(0,len(input_list),3)]    
    return res

def get_points(rep):
	points = 0
	for char in rep:
		points += 1+string.ascii_lowercase.index(char.lower())
		points += 26 if char != char.lower() else 0
	return points

def part1(input_list):
	rep = []
	for l in input_list:
		rep += list(set([c for c in l[0] if c in l[1]]))
	print("Part 1 solution:", get_points(rep))

def part2(input_list):
	rep = []
	for l in input_list:
		rep += list(set([c for c in l[0] if c in l[1] and c in l[2]]))
	print("Part 2 solution:", get_points(rep))


if __name__ == '__main__':
    input_list = open(sys.argv[1], "r").read().split("\n")
    
    cleaned_list = clean_for_part1(input_list)
    part1(cleaned_list)

    cleaned_list = clean_for_part2(input_list)
    part2(cleaned_list)
