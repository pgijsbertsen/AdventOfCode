import os

# Get the input
input = open(os.path.dirname(__file__) + "/inputs/input.txt", "r").readlines()

# Do the magic
def split_input(input: list[str]) -> tuple[list[int], list[int]]:
    left = []
    right = []

    for line in input:
        left.append(int(line.split("   ")[0].strip()))
        right.append(int(line.split("   ")[1].strip()))

    return left, right

def find_distance(input: tuple[list[int], list[int]]) -> int:
    left = sorted(input[0])
    right = sorted(input[1])

    sum_list = [ abs(l - r) for l, r in zip(left, right) ]

    sum = 0
    for i in sum_list:
        sum += i

    return sum

def get_sim_score(input: tuple[list[int], list[int]]) -> int:
    left = input[0]
    right = input[1]

    sum_score = []
    multiply = 0
    for i in left:
        if i in right:
            multiply = right.count(i)
            sum_score.append(i * multiply)

    return sum(sum_score)
        
# Return the magic
print("Part One: " + str(find_distance(split_input(input))))
print("Part Two: " + str(get_sim_score(split_input(input))))
