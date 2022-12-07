import sys 


def solution(input_list):
    cwd = '/'
    dir_sizes = {'/': 0}
    stack = []

    # Get sizes only from current directory files
    for command in input_list:
        if command.startswith('$ cd'):
            new_dir = command[5:].strip()
            if new_dir == '/':
                cwd = '/'
                stack = []
            elif new_dir == '..':
                if stack:
                    cwd = stack.pop()
            else:
                stack.append(cwd)
                cwd = cwd + '/' + new_dir
                if cwd not in dir_sizes:
                    dir_sizes[cwd] = 0
        elif command.startswith('$ ls'):
            pass
        else:
            if not command.startswith('dir'):
                size = int(command.split(' ')[0])
                dir_sizes[cwd] += size
            else:
                item = command[3:].strip()
                if cwd + '/' + item not in dir_sizes:
                    dir_sizes[cwd + '/' + item] = 0

    # Sum directory sizes from children as well
    for key in dir_sizes.keys():
        dir_sizes[key] = sum([dir_sizes[k] for k in dir_sizes.keys() if key in k])

    sum_below_100k = sum([v for v in dir_sizes.values() if v<100000])
    print("Solution part 1:", sum_below_100k)

    dir_sizes = dir_sizes.values()
    size_used = max(dir_sizes)
    needed_size_to_delete = 30000000-(70000000-size_used)
    size_to_delete = min([v for v in dir_sizes if v > needed_size_to_delete])
    print("Solution part 2:", size_to_delete)

    
if __name__ == '__main__':
    input_list = open(sys.argv[1], "r").read().split("\n")
    solution(input_list)

