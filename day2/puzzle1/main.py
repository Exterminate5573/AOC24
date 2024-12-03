
total_safe = 0

with open("day2/input.txt") as input:
    for line in input.readlines():
        numlist = []
        for i in line.split(" "):
            numlist.append(int(i))

        is_first = True
        is_safe = True
        is_increasing = True
        for i in range(len(numlist) - 1):
            num1 = numlist[i]
            num2 = numlist[i + 1]

            if is_first:
                if num1 < num2:
                    is_increasing = True
                elif num1 > num2:
                    is_increasing = False
                else:
                    is_safe = False
                    break

                is_first = False

            if is_increasing:
                if num1 >= num2:
                    is_safe = False
                    break
                else:
                    diff = num2 - num1

                    if diff > 3:
                        is_safe = False
                        break
            else:
                if num1 <= num2:
                    is_safe = False
                    break
                else:
                    diff = num1 - num2

                    if diff > 3:
                        is_safe = False
                        break
        
        if is_safe:
            total_safe += 1


print(total_safe)