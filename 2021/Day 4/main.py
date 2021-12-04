
def get_boards(lines):
    boards = []
    board = []
    for line in lines:
        if line!='':
            cleaned_line = [(l, 0) for l in line.split(" ") if l!='']
            board.append(cleaned_line)
        else:
            boards.append(board)
            board = []
    boards.append(board)
    return boards

def part1(bingo, boards):
    # To take account of total elements called. 1st list counts in each row, 2nd list count in columns
    called_boards = [[[0,0,0,0,0], [0,0,0,0,0]] for _ in range(len(boards))]
    finish = False
    board_winner = 0
    
    # Update numbers called in boards and finish when a winner found
    for number in bingo:
        for board in range(0, len(boards)):
            for row in range(0, len(boards[board])):
                for column in range(0, len(boards[board][row])):
                    if boards[board][row][column][0]==number:
                        boards[board][row][column] = (number, 1)
                        called_boards[board][0][row]+=1
                        called_boards[board][1][column]+=1
                        if (called_boards[board][0][row] == 5) | (called_boards[board][1][column] == 5):
                            finish = True
                            board_winner = board
                            break
                if finish: break
            if finish: break
        if finish: break
    
    # Get score
    score = 0
    for row in range(0, len(boards[board_winner])):
                for column in range(0, len(boards[board_winner][row])):
                    if boards[board_winner][row][column][1]==0:
                        score += int(boards[board_winner][row][column][0])
    
    print(score*int(number))
        
def part2(bingo, boards):
    # To take account of total elements called. 1st list counts in each row, 2nd list count in columns
    called_boards = [[[0,0,0,0,0], [0,0,0,0,0]] for _ in range(len(boards))]
    winners = [0]*len(boards)
    finish = False
    
    # Update numbers called in boards and finish when last winner found
    for number in bingo:
        for board in range(0, len(boards)):
            for row in range(0, len(boards[board])):
                for column in range(0, len(boards[board][row])):
                    if boards[board][row][column][0]==number:
                        boards[board][row][column] = (number, 1)
                        called_boards[board][0][row]+=1
                        called_boards[board][1][column]+=1
                        if (called_boards[board][0][row] == 5) | (called_boards[board][1][column] == 5):
                            last_board_winner = boards[board].copy()
                            last_number_winner = number
                            winners[board] = 1
                            if sum(winners)==len(boards):
                                finish = True
                                break
                if finish: break
            if finish: break
        if finish: break
    
    # Get score
    score = 0
    for row in range(0, len(last_board_winner)):
                for column in range(0, len(last_board_winner[row])):
                    if last_board_winner[row][column][1]==0:
                        score += int(last_board_winner[row][column][0])
    
    print(score*int(last_number_winner))
        
    
    
if __name__ == '__main__':
    lines = open("2021/Day 4/input.txt", "r").read().split("\n")
    bingo = lines[0].split(',')
    boards = get_boards(lines[2:]) # Aux function to get boards as list of lists, with tuples in format (number, called)
    part1(bingo, boards)
    part2(bingo, boards)