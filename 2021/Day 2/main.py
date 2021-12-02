
def part1(input_list):
    distance, depth = 0, 0
    
    for i in range(0,len(input_list)):
            if input_list[i][0] == 'forward':
                distance+=int(input_list[i][1])
            elif input_list[i][0] == 'up':
                depth-=int(input_list[i][1])
            elif input_list[i][0] == 'down':
                depth+=int(input_list[i][1])
            else:
                print("Error")
        
    print(distance*depth)

def part2(input_list):
    distance, depth, aim = 0, 0, 0
    
    for i in range(0,len(input_list)):
            if input_list[i][0] == 'forward':
                distance+=int(input_list[i][1])
                depth+=(int(input_list[i][1]) * aim)
            elif input_list[i][0] == 'up':
                aim-=int(input_list[i][1]) 
            elif input_list[i][0] == 'down':
                aim+=int(input_list[i][1])
            else:
                print("Error")
        
    print(distance*depth)

if __name__ == '__main__':
    input_list = open("2021/Day 2/input.txt", "r").read().split("\n")
    input_list = [x.split(" ") for x in input_list]
    part1(input_list)
    part2(input_list)