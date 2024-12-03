import re

#IK i cheated a little bit by adding a do() to the start of the file but idrc

regex = r"(do\(\)(.\s?(?!don't\(\)))*mul\([0-9][0-9]?[0-9]?,[0-9][0-9]?[0-9]?\))"
regex2 = r"mul\([0-9][0-9]?[0-9]?,[0-9][0-9]?[0-9]?\)"

total = 0

with open("day3/input.txt") as input:
    cases = re.findall(regex, input.read())

    for l in cases:
        cases2 = re.findall(regex2, l[0])

        for i in cases2:
            i = str(i)

            i = i.removeprefix("mul(")
            i = i.removesuffix(")")

            num1 = int(i.split(",")[0].replace(",", ""))
            num2 = int(i.split(",")[1].replace(",", ""))

            product = num1 * num2

            total += product
        

print(total)