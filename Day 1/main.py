input_list = open("Day 1/input.txt", "r").read().split("\n")

previous_item = None
count=0
for item in input_list:
    if (previous_item is not None):
        if item>previous_item:
            count+=1
    previous_item=item
    
print(count)
