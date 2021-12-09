

def get_translations(inputs):
    nums_unique_len = {2:1, 4:4, 3:7, 7:8}
    input_translate = ['' if len(x) not in nums_unique_len.keys() else nums_unique_len[len(x)] for x in inputs]
    
    # Dictionary of 7 segment display (a,b,c,d,e,f,g) reassignments
    dict_positions = {'a':'','b':'', 'c':'', 'd':'', 'e':'', 'f':'', 'g':''}
    
    # To get upper led (position a), we have to get the led that is used in 7 but not in 1
    dict_positions['a'] = list(set(inputs[input_translate.index(7)]) - set(inputs[input_translate.index(1)]))[0]
    
    # Now we want to know which value represents the 6. To do that, we get the values that use 6 leds (0, 6 and 9), and the one that does not have two leds in common with 1,
    # is the 6. And then we will be able to assign possitions b (led in common between 1 and 6), and c after that.
    pos_six = [x for x in inputs if (len(set(inputs[input_translate.index(1)])-set(x))==1) & (len(x)==6)][0]
    input_translate[inputs.index(pos_six)] = 6
    
    dict_positions['b'] = list(set(inputs[input_translate.index(1)]) - set(pos_six))[0]
    dict_positions['c'] = list(set(inputs[input_translate.index(1)]) - {dict_positions['b']})[0]
    
    # It's the turn to get which is the 3, by getting the value that shares led's with 7 and length=5. Then, the led that is not used in 4 and 7,
    # and that is used in 3, will be d, and the other one the g (by discard). And if we use 4 and remove the leds we already know, we get f, and the one missing is e
    pos_three = [x for x in inputs if (len(set(inputs[input_translate.index(7)])-set(x))==0) & (len(x)==5)][0]
    input_translate[inputs.index(pos_three)] = 3
    
    dict_positions['d'] = list((set(pos_three) - set(inputs[input_translate.index(7)])) - set(inputs[input_translate.index(4)]))[0]
    dict_positions['g'] = list(set(pos_three) - set(dict_positions.values()))[0]
    dict_positions['f'] = list(set(inputs[input_translate.index(4)]) - set(dict_positions.values()))[0]
    dict_positions['e'] = list({'a','b','c','d','e','f','g'} - set(dict_positions.values()))[0]
    
    dict_positions = {v: k for k, v in dict_positions.items()}  # Invert dict
    return dict_positions
    

def get_numbers_from_line(input_line):
    inputs, outputs = input_line.split(" | ")[0].split(" "), input_line.split(" | ")[1].split(" ")
    dict_positions = get_translations(inputs) 
    correct_leds = {
            0:{'a','b','c','d','e','f'}, 1:{'b','c'}, 2:{'a','b','d','e','g'}, 3:{'a','b','c','d','g'}, 4:{'b','c','f','g'}, 5:{'a','c','d','f','g'}, 
            6:{'a','c','d','e','f','g'}, 7: {'a','b','c'}, 8:{'a','b','c','d','e','f','g'}, 9:{'a','b','c','d','f','g'}
            }
    
    result = ''
    for i in range(0, len(outputs)):
        active_leds = [dict_positions[x] for x in outputs[i]]
        for number in correct_leds.keys():
            if set(active_leds) == correct_leds[number]:
                result += str(number)
            
    return int(result)


def get_total_1_4_7_8(input_l):
    input_list_outputs = [l.split(" | ")[1] for l in input_l]
    input_list = [l.split(" ") for l in input_list_outputs]
    
    dict_numbers = {1:2, 4:4, 7:3, 8:7}
    unique_len = list(dict_numbers.values())
    
    total_uniques = sum([1 if len(x) in unique_len else 0 for line in input_list for x in line])
    
    print("Total of 1, 4, 7 and 8:",total_uniques)
    
    
def get_total_of_outputs(input_l):
    total = sum([get_numbers_from_line(line) for line in input_l])
    print("Total sum:", total)
    
    
if __name__ == '__main__':
    input_l = open("2021/Day 8/input.txt", "r").read().split("\n")
    get_total_1_4_7_8(input_l)
    get_total_of_outputs(input_l)    