import sys 

def clean(input_list):
    cleaned_list = [line.split(' ') for line in input_list if len(line.split(' '))>1]
    return cleaned_list

def result(a,b):
    res_dic = {
		('A','X'): 3, ('A','Y'): 6, ('A','Z'): 0, 
        ('B','X'): 0, ('B','Y'): 3, ('B','Z'): 6,
		('C','X'): 6, ('C','Y'): 0, ('C','Z'): 3		
	 }

    return res_dic[(a,b)]

    
def part1(input_list):
    acum = 0
    for x in input_list:
        res = result(x[0],x[1])
        res += 3 if x[1]=='Z' else 2 if x[1]=='Y' else 1
        acum += res
        print(acum, res)

    print("Part 1 solution: ", acum)

    
def part2(input_list):
    acum = 0
    dict_result = {'X': 0, 'Y': 3, 'Z': 6}
    for x in input_list:
        for possible_result in ['X','Y','Z']:
            if dict_result[x[1]]==result(x[0],possible_result):
                break
        res = dict_result[x[1]]   
        res += 3 if possible_result=='Z' else 2 if possible_result=='Y' else 1
        acum += res

    print("Part 2 solution: ", acum)


if __name__ == '__main__':
    input_list = open(sys.argv[1], "r").read().split("\n")

    cleaned_list = clean(input_list)
    part1(cleaned_list)
    part2(cleaned_list)
