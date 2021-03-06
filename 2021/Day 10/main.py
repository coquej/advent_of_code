close_chunk = {"[":"]", "{":"}", "(":")", "<":">" }
negative_points = {"]":57, "}":1197, ")":3, ">":25137}
score_points = {"]":2, "}":3, ")":1, ">":4}
    
    
def is_corrupted(line):
    list_open_chunks = []
    
    for chunk in line:
        if chunk in close_chunk.keys():
            list_open_chunks.append(chunk)
        elif close_chunk[list_open_chunks[-1]]!=chunk:
            return True, chunk
        else:
            list_open_chunks.pop()
            
    return False, None

def get_points_from_corrupted(lines):
    points = 0
    for line in lines:
        line_is_corrupted, chunk_received = is_corrupted(line)
        if line_is_corrupted:
            points += negative_points[chunk_received]
    
    print("Total syntax error score (part 1):", points)

def get_score_from_line(missing_chunks):
    score = 0
    
    for chunk in missing_chunks:
        score=(score*5 + score_points[chunk])
    
    return score

def get_middle_score(lines):
    cleaned_lines = [line for line in lines if not (is_corrupted(line)[0])]
    points = []
    
    for line in cleaned_lines:
        list_open_chunks = []
        for chunk in line:
            if chunk in close_chunk.keys():
                list_open_chunks.append(chunk)
            else:
                _ = list_open_chunks.pop()
        list_open_chunks.reverse()
        missing_chunks = [close_chunk[char] for char in list_open_chunks]
        points += [get_score_from_line(missing_chunks)]
    
    points.sort()
    
    print("Middle score (part 2):", points[int(len(points)/2)])
    

if __name__ == '__main__':
    lines = [line for line in open("2021/Day 10/input.txt", "r").read().split("\n")]
    get_points_from_corrupted(lines)
    get_middle_score(lines)  