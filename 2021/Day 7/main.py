
def sum_arithmetic(a,b):
    return abs(a-b)*(abs(a-b)+1)//2

def get_position_part1(crabs):
    fuel = float('inf')
    
    for crab in range(min(crabs), max(crabs) + 1):
        fuel_to_position = sum(map(lambda p: abs(crab-p), crabs))
        fuel = min(fuel, fuel_to_position)
    
    print("Fuel:", fuel)
            
def get_position_part2(crabs):
    fuel = float('inf')
    
    for crab in range(min(crabs), max(crabs) + 1):
        fuel_to_position = sum(map(lambda p: sum_arithmetic(crab, p), crabs))
        fuel = min(fuel, fuel_to_position)
    
    print("Fuel:", fuel)

    
if __name__ == '__main__':
    crabs = [int(l) for l in open("2021/Day 7/input.txt", "r").read().split(",")]
    get_position_part1(crabs)
    get_position_part2(crabs)