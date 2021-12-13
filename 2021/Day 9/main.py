import math

def is_basin(i,  j,  lines):
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
    basins = []
    
    for i in range(len(lines)):
        for j in range(len(lines[i])):
           if is_basin(i, j, lines):
               risk += [(lines[i][j] + 1)]
               basins.append((i,j))
    
    print("Risk:", sum(risk))
    return basins


def get_new_to_explore(i, j, lines):
    if i==0:
        if j==0:
            possible_elements_to_explore = [(i+1,j), (i,j+1)]
        elif j==(len(lines[i])-1):
            possible_elements_to_explore = [(i+1,j), (i,j-1)]
        else:
            possible_elements_to_explore = [(i+1,j), (i,j-1), (i,j+1)]
        
    elif i==(len(lines)-1):
        if j==0:
            possible_elements_to_explore = [(i-1,j), (i,j+1)]
        elif j==(len(lines[i])-1):
            possible_elements_to_explore = [(i-1,j), (i,j-1)]
        else:
            possible_elements_to_explore = [(i-1,j), (i,j-1), (i,j+1)]
        
    elif j==0:
        possible_elements_to_explore = [(i-1,j), (i+1,j), (i,j+1)]
    
    elif j==(len(lines[i])-1):
        possible_elements_to_explore = [(i-1,j), (i+1,j), (i,j-1)]
    
    else:
        possible_elements_to_explore = [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]
    
    return [(a,b) for a,b in possible_elements_to_explore if (lines[a][b]>(lines[i][j])) and (lines[a][b]!=9)]
    
    
def get_size_from_basins(basins, lines):
    sizes = []
    all_explored=set()
    
    for basin in basins:
        already_explored = set()
        to_explore = {basin}
        while len(to_explore) > 0:
            x = list(to_explore)[0]
            all_explored.add(x)
            already_explored.add(x)
            to_explore.remove(x)
            new_to_explore = get_new_to_explore(x[0], x[1], lines)
            for new in new_to_explore:
                if new not in list(all_explored):
                    to_explore.add(new)
        sizes.append(len(already_explored))
    
    sizes.sort(reverse=True)
    print("Multiplication:", math.prod(sizes[:3]))
    
    
if __name__ == '__main__':
    lines = [[int(char) for char in line] for line in open("2021/Day 9/input.txt", "r").read().split("\n")]
    basins = get_risk_levels(lines)
    get_size_from_basins(basins, lines)     