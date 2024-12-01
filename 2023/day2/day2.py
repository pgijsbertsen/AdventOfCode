# Read input
input = open("inputs/input.txt", "r").read().split('\n')

max_cubes = {
    'red' : 12,
    'green' : 13,
    'blue' : 14
    }

# Do stuff
def puzzle1():
    idsum = 0
    for line in input:
        game = line.split(":")
        gamenum = int(game[0].split()[1])
        draws = game[1].split(";")
        for draw in draws:
            cubes = draw.split(",")
            for cube in cubes:
                if int(cube.split()[0]) > max_cubes[cube.split()[1]]:
                    break
            else:
                continue
            break
        else:
            idsum += gamenum
    return(idsum)

def puzzle2(row):
    rMax = 0
    gMax = 0
    bMax = 0
    game = row.split(":")
    gamenum = int(game[0].split()[1])
    draws = game[1].split(";")
    for draw in draws:
        cubes = draw.split(',')
        for cube in cubes:
            rgb = cube.split(' ')
            num = int(rgb[1])
            color = rgb[2]
            if color == "red":
                if num > rMax:
                    rMax = num
            if color == "green":
                if num > gMax:
                    gMax = num
            if color == "blue":
                if num > bMax:
                    bMax = num
    power = rMax * gMax * bMax
    return power

# Gather and print results
result1 = puzzle1()
result2 = 0
for line in input:
    result2 += puzzle2(line)
print('Result 1:', result1, '\nResult 2:', result2)