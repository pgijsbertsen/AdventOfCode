# Read input
input = open("inputs/input.txt", "r").read().split('\n')

# Do stuff
def puzzle1(inputRows):
    totalPoints = 0
    for card in inputRows:
        winningNumbers = (card.split(' | ')[0]).split(' ')
        myNumbers = (card.split(' | ')[1]).split(' ')
        wonNumbers = []
        points = 0
        for myNumber in myNumbers:
            if myNumber in winningNumbers and myNumber != '':
                wonNumbers.append(myNumber)
            totalWonNumbers = len(wonNumbers)
        for wonNumber in wonNumbers:
            if points == 0:
                points = 1
            else:
                points *= 2
        totalPoints += points
    return(totalPoints)

# Print output
result = puzzle1(input)
print('Result:', result)