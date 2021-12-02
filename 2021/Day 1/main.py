
def part1(input_list):
    count=0
    for i in range(1,len(input_list)):
            if int(input_list[i])>int(input_list[i-1]):
                count+=1
        
    print(count)

def part2(input_list):
    count=0
    for i in range(3,len(input_list)):
            if (int(input_list[i])+int(input_list[i-1])+int(input_list[i-2]))>\
                int(input_list[i-1])+int(input_list[i-2])+int(input_list[i-3]):
                count+=1
        
    print(count)


if __name__ == '__main__':
    input_list = open("2021/Day 1/input.txt", "r").read().split("\n")
    part1(input_list)
    part2(input_list)