import math
            
def get_total_fishes_after_x_days(lanternfishes, days):
    fishes = lanternfishes.copy()
    
    dict_fishes = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
    
    for fish in fishes:
        dict_fishes[fish] += 1
        
    for _ in range(0,days):
        new_fishes = dict_fishes[0]
        for days_to_generate in range(0, 8):
            dict_fishes[days_to_generate] = dict_fishes[days_to_generate+1]
        dict_fishes[6] += new_fishes
        dict_fishes[8] = new_fishes
    
    print("Total lanternfishes:", sum(dict_fishes.values()))
    
if __name__ == '__main__':
    lanternfishes = [int(l) for l in open("2021/Day 6/input.txt", "r").read().split(",")]
    get_total_fishes_after_x_days(lanternfishes,days=256)