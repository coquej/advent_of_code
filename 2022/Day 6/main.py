import sys 


def solution(input_list, part):
    tot_chars = 4 if part==1 else 14
    for i in range(tot_chars-1, len(input_list)):
        if len(set(input_list[i-(tot_chars-1):i+1]))==tot_chars:
            print("Solution part", part, ":", i+1)
            break
        
    
if __name__ == '__main__':
    input_list = open(sys.argv[1], "r").read()
    solution(input_list, 1)
    solution(input_list, 2)

