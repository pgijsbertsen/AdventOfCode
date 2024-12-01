import numpy as np

# Read input
input = open("inputs/example_input.txt", "r").read().split('\n')

# Do stuff
def puzzle1(rows):
    find = '*'
    rowList = [list(row) for row in rows]
    print('Rows:', rows)
    #print('Grid:', np.array(rowlist))
    for index, value in enumerate(rowList):
        subIndex = ''
        print('Index, value:', index, value)
        if find in value:
           subIndex = value.index(find)
           print('Subindex:', subIndex)
           break




# Gather and print results
result = puzzle1(input)