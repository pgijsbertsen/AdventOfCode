import os
import re

# Get the input
input = open(os.path.dirname(__file__) + "/inputs/input.txt", "r").readlines()

# Do the magic
class Mul():

    use_mul: bool = True

    def extract_muls(self, line: str, filtered: bool) -> list[str]:
        if filtered:
            pattern = r"do\(\)|don't\(\)|mul\(\d+,\d+\)"
            muls: list[str] = []

            for mul in re.findall(pattern, line):

                if mul == "don't()":
                    self.use_mul = False

                if mul == "do()":
                    self.use_mul = True
                    continue

                if self.use_mul:
                    muls.append(mul)

            return muls

        else:
            pattern = re.compile(r'mul\(\d{1,3},\d{1,3}\)')
            return re.findall(pattern, line)

    def multiply_muls(self, input: list[str], filtered: bool) -> int:
        result: int = 0
        input_muls: list[str] = []

        for line in input:
            input_muls += self.extract_muls(line, filtered)

        for mul in input_muls:
            digits = re.findall(r'\d{1,3}', mul)
            result += int(digits[0]) * int(digits[1])

        return result

# Return the magic
mul = Mul()
print("Part One: " + str(mul.multiply_muls(input, False)))
print("Part Two: " + str(mul.multiply_muls(input, True)))
