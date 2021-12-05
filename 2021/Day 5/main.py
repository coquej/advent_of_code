
def part1(lines, max_rows, max_cols):
    matrix = [[0]*max_rows for _ in range(max_cols)]
    
    for line in lines:
        if line[0][0]==line[1][0]:
            min_val = min([int(line[0][1]),int(line[1][1])])
            max_val = max([int(line[0][1]),int(line[1][1])])+1
            for it in range(min_val, max_val):
                matrix[it][int(line[0][0])]+=1
        elif line[0][1]==line[1][1]:
            min_val = min([int(line[0][0]),int(line[1][0])])
            max_val = max([int(line[0][0]),int(line[1][0])])+1
            for it in range(min_val, max_val):
                matrix[int(line[0][1])][it]+=1
                
    count = sum([1 if column>=2 else 0 for row in matrix for column in row])

    print(count)
            
            
def part2(lines, max_rows, max_cols):
    matrix = [[0]*max_rows for _ in range(max_cols)]
    
    for line in lines:
        if line[0][0]==line[1][0]:
            min_val = min([int(line[0][1]),int(line[1][1])])
            max_val = max([int(line[0][1]),int(line[1][1])])+1
            for it in range(min_val, max_val):
                matrix[it][int(line[0][0])]+=1
        elif line[0][1]==line[1][1]:
            min_val = min([int(line[0][0]),int(line[1][0])])
            max_val = max([int(line[0][0]),int(line[1][0])])+1
            for it in range(min_val, max_val):
                matrix[int(line[0][1])][it]+=1
        else:
            min_x = min([int(line[0][0]),int(line[1][0])])
            max_x = max([int(line[0][0]),int(line[1][0])])
            min_y = min([int(line[0][1]),int(line[1][1])])
            max_y = max([int(line[0][1]),int(line[1][1])])
            x, y = int(line[0][0]),int(line[0][1])
            op_x = 'suma' if x==min_x else 'resta'
            op_y = 'suma' if y==min_y else 'resta'
            
            matrix[y][x]+=1
            while not ((x == int(line[1][0])) & (y == int(line[1][1]))):
                x = x + 1 if op_x == 'suma' else x - 1
                y = y + 1 if op_y == 'suma' else y - 1
                matrix[y][x]+=1
                
    count = sum([1 if column>=2 else 0 for row in matrix for column in row])

    print(count)

    
if __name__ == '__main__':
    lines = open("2021/Day 5/input.txt", "r").read().split("\n")
    lines = [[tup.split(",") for tup in line.split(' -> ')] for line in lines]
    max_rows = max([max([int(line[0][0]),int(line[1][0])]) for line in lines])+1
    max_cols = max([max(int(line[0][1]),int(line[1][1])) for line in lines])+1
    part1(lines, max_rows, max_cols)
    part2(lines, max_rows, max_cols)