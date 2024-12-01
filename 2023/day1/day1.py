# Read input
input = open("inputs/input.txt", "r")

# Do stuff
def sum_digits():
    sum_input = []
    for line in input:
        stripped_line = ''.join(i for i in line if i.isdigit())
        first_digit = stripped_line[0]
        last_digit = stripped_line[-1]
        digits = first_digit + last_digit
        sum_input.append(int(digits))
    return sum(sum_input)

def sum_chars():
    sum_input = []
    numbers = {'one' : 'o1ne', 'two' : 't2wo', 'three' : 'th3ree', 'four' : 'fo4ur', 'five' : 'fi5ve', 'six' : 's6ix', 'seven' : 'se7ven', 'eight' : 'eig8ht', 'nine' : 'ni9ne'}
    for line in input:
        for word, number in numbers.items():
            line = line.replace(word, number)
        stripped_line = ''.join(i for i in line if i.isdigit())
        first_digit = stripped_line[0]
        last_digit = stripped_line[-1]
        digits = first_digit + last_digit
        sum_input.append(int(digits))
    return sum(sum_input)

# Print result
result = sum_chars()
print('Result: ', result)