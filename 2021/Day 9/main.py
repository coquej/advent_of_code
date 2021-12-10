
def is_low_point(i,  j,  lines):
    if i==0:
        if j==0:
            return min([lines[i+1][j], lines[i][j+1]]) > lines[i][j]
        elif j==(len(lines[i])-1):
            return min([lines[i+1][j], lines[i][j-1]]) > lines[i][j]
        else:
            return min([lines[i+1][j], lines[i][j-1], lines[i][j+1]]) > lines[i][j]
        
    elif i==(len(lines)-1):
        if j==0:
            return min([lines[i-1][j], lines[i][j+1]]) > lines[i][j]
        elif j==(len(lines[i])-1):
            return min([lines[i-1][j], lines[i][j-1]]) > lines[i][j]
        else:
            return min([lines[i-1][j], lines[i][j-1], lines[i][j+1]]) > lines[i][j]
        
    elif j==0:
        return min([lines[i-1][j], lines[i+1][j], lines[i][j+1]]) > lines[i][j]
    
    elif j==(len(lines[i])-1):
        return min([lines[i-1][j], lines[i+1][j], lines[i][j-1]]) > lines[i][j]
    
    else:
        return min([lines[i-1][j], lines[i+1][j], lines[i][j-1], lines[i][j+1]])  >  lines[i][j]
            

def get_risk_levels(lines):
    risk = []
    
    for i in range(len(lines)):
        for j in range(len(lines[i])):
           if is_low_point(i, j, lines):
               risk += [(lines[i][j] + 1)]
    
    print("Risk:", sum(risk))

    
if __name__ == '__main__':
    lines = [[int(char) for char in line] for line in open("2021/Day 9/input.txt", "r").read().split("\n")]
    get_risk_levels(lines)
     