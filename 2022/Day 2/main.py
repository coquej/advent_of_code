import sys 

def clean(input_list):
    cleaned_list = [line.split(' ') for line in input_list if len(line.split(' '))>1]
    return cleaned_list

def result(a,b):
    res_dic = {
		('A','X'): 3,
		('A','Y'): 0,
		('A','Z'): 6,
		('B','X'): 6,
		('B','Y'): 3,
		('B','Z'): 0,
		('C','X'): 0,
		('C','Y'): 6,
		('C','Z'): 3		
	      }
    return res_dic[(a,b)]
    
def part1(input_list):
    acum = 0
    for x in input_list:
        res = result(x[0],x[1])
        res += 3 if x[0]=='C' else 2 if x[0]=='B' else 1
        acum+=res

    print("Part 1 solution: ", acum)


if __name__ == '__main__':
    input_list = open(sys.argv[1], "r").read().split("\n")

    cleaned_list = clean(input_list)
    print(part1(cleaned_list))
