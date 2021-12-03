
def part1(input_list_ori):
    input_list = [list(map(int, list(i))) for i in zip(*input_list_ori)]
    gamma, epsilon = '', ''
    
    for i in range(0,len(input_list)):
            gamma += str(max(set(input_list[i]), key = input_list[i].count))
            epsilon += str(min(set(input_list[i]), key = input_list[i].count))
        
    gamma, epsilon = int(gamma, 2), int(epsilon, 2)
    
    print(gamma*epsilon)
    
    
def part2(input_list_ori):
    ox, co2 = input_list, input_list

    i = 0
    while len(ox)>1:
        zeros, ones = 0, 0
        
        for item in ox:
            if int(item[i]) == 0:
                zeros += 1
            else:
                ones += 1
                
        ox = [x for x in ox if int(x[i])==1] if ones>=zeros else [x for x in ox if int(x[i])==0] 
        i+=1
        
    i = 0
    while len(co2)>1:
        zeros, ones = 0, 0
        
        for item in co2:
            if int(item[i]) == 0:
                zeros += 1
            else:
                ones += 1
                
        co2 = [x for x in co2 if int(x[i])==1] if ones<zeros else [x for x in co2 if int(x[i])==0]
        i+=1
    
    ox, co2 = int(ox[0], 2), int(co2[0], 2)
    
    print(ox*co2)


if __name__ == '__main__':
    input_list = open("2021/Day 3/input.txt", "r").read().split("\n")
    part1(input_list)
    part2(input_list)