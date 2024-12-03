import re

regex = r"mul\([0-9][0-9]?[0-9]?,[0-9][0-9]?[0-9]?\)"

total = 0

with open("day3/input.txt") as input:
    cases = re.findall(regex, input.read())

    for i in cases:
        i = str(i)

        i = i.removeprefix("mul(")
        i = i.removesuffix(")")

        num1 = int(i.split(",")[0].replace(",", ""))
        num2 = int(i.split(",")[1].replace(",", ""))

        product = num1 * num2

        total += product
        

print(total)