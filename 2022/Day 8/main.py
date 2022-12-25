import sys 
import math as np

def clean_input(input_list):
    return [[int(y) for y in x] for x in input_list]

def is_visible(i, j, trees):
    check_left = [trees[i][x] for x in range(0,j)]
    check_right = [trees[i][x] for x in range(j+1,len(trees[0]))]
    check_up = [trees[x][j] for x in range(0,i)]
    check_down = [trees[x][j] for x in range(i+1,len(trees))]
        
    return any([all([trees[i][j]>tree for tree in check]) for check in [check_left, check_right, check_up, check_down]])

def get_visible_trees(trees):
    outer_visibles = 2*(len(trees)-1)+2*(len(trees[0])-1)
    inner_visibles = sum([is_visible(i,j,trees) for i in range(1,len(trees)-1) for j in range(1,len(trees[i])-1)])

    print('There are', outer_visibles+inner_visibles, 'visible trees')

def get_score(i, j, trees):
    check_left = [trees[i][x] for x in range(j-1,-1,-1)]
    check_right = [trees[i][x] for x in range(j+1,len(trees[0]))]
    check_up = [trees[x][j] for x in range(i-1,-1,-1)]
    check_down = [trees[x][j] for x in range(i+1,len(trees))]

    total = 1
    for check in [check_left, check_right, check_up, check_down]:
        trees_seen = 0
        for t in range(len(check)):
            if trees[i][j]>check[t]:
                trees_seen += 1 # another smaller tree
            else:
                trees_seen += 1 # first higher tree, so last tree to see
                break
        total *= trees_seen

    return total

def get_max_score(trees):
    max_score = max([get_score(i,j,trees) for i in range(0,len(trees)) for j in range(0,len(trees[i]))])
    print('The greatest score is', max_score)


if __name__ == '__main__':
    input_list = open(sys.argv[1], "r").read().split("\n")
    trees = clean_input(input_list)
    get_visible_trees(trees)
    get_max_score(trees)

