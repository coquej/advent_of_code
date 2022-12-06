import sys 
import string


def clean_list(input_list):
    res = [[l.split(',')[0].split('-'),l.split(',')[1].split('-')] for l in input_list ]
    return res

def is_contained_in(a,b):
	b_range = range(int(b[0]),int(b[1])+1)
	return (int(a[0]) in b_range) & (int(a[1]) in b_range)

def overlaps(a,b):
	b_range = range(int(b[0]),int(b[1])+1)
	return (int(a[0]) in b_range) | (int(a[1]) in b_range)

def part1(input_list):
	contained_l = [is_contained_in(x[0],x[1]) | is_contained_in(x[1],x[0]) for x in input_list]
	print('Part 1 solution:', sum(contained_l))

def part2(input_list):
	overlaps_l = [overlaps(x[0],x[1]) | overlaps(x[1],x[0]) for x in input_list]
	print('Part 2 solution:', sum(overlaps_l))

if __name__ == '__main__':
    input_list = open(sys.argv[1], "r").read().split("\n")    
    cleaned_list = clean_list(input_list)
    part1(cleaned_list)
    part2(cleaned_list)
