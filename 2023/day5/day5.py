# Read input
input = open("inputs/example_input.txt", "r").read().split('\n\n')

# Do stuff

def get_destination(destStart, sourceStart, rangeLength):
    return()

def puzzle1(inputRows):
    print('inputRows:', inputRows)
    for row in inputRows:
        if 'seeds' in row:
            destIn = (row.split(': ')[1]).split(' ')
            print('seeds:', destIn)
        else:
            maps = (row.split('\n'))
            locations = []
            print(row)
            print('maps:', maps)
            for map in maps:
                if destIn in map:
                    print('Seed found in', map)

# Print output
result = puzzle1(input)
print('Result:', result)