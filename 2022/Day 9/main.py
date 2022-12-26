import sys 

def move_head(h_pos, dir):
    if dir=='U':
        return (h_pos[0], h_pos[1]+1)
    elif dir=='D':
        return (h_pos[0], h_pos[1]-1)
    elif dir=='R':
        return (h_pos[0]+1, h_pos[1])
    else:
        return (h_pos[0]-1, h_pos[1])

def positions_visited(instructions):
    visited = {(0,0)}
    h_pos=(0,0)
    t_pos=(0,0)
    for instr in instructions:
        for _ in range(instr[1]):
            h_new_pos = move_head(h_pos, instr[0])
            t_pos = h_pos if (abs(h_new_pos[0]-t_pos[0])>1) | (abs(h_new_pos[1]-t_pos[1])>1) else t_pos
            visited.add(t_pos)
            h_pos = h_new_pos
    
    print("Positions visited:", len(visited))

def move_nearest(to_follow, to_move):
    delta_x = to_follow[0]-to_move[0]
    delta_y = to_follow[1]-to_move[1]

    if (abs(delta_x)<=1) & (abs(delta_y)<=1):
        return to_move
    if abs(delta_x) < abs(delta_y):
        return (to_follow[0], to_move[1] + delta_y // abs(delta_y))
    elif abs(delta_x) > abs(delta_y):
        return (to_move[0] + delta_x // abs(delta_x), to_follow[1])
    else:
        return to_follow[0] - delta_x // abs(delta_x), to_follow[1] - delta_y // abs(delta_y )
    
def positions_visited_2(instructions):
    visited = {(0,0)}
    rope = [(0,0) for _ in range(10)]
    for instr in instructions:
        for _ in range(instr[1]):
            rope[0] = move_head(rope[0], instr[0])
            for k in range(1,10):
                rope[k] = move_nearest(rope[k-1], rope[k])
                if k==9:
                    visited.add(rope[k])
                        
    print("Positions visited:", len(set(visited)))

if __name__ == '__main__':
    input_list = open(sys.argv[1], "r").read().split("\n")
    instructions = [[x.split()[0], int(x.split()[1])] for x in input_list]

    positions_visited(instructions)
    positions_visited_2(instructions)


