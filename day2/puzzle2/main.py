
#WIP

def check_vals(num1, num2, is_first, is_increasing):
    if is_increasing:
        if num1 >= num2:
            is_safe = False
        else:
            diff = num2 - num1

            if diff > 3:
                is_safe = False
    else:
        if num1 <= num2:
            is_safe = False
        else:
            diff = num1 - num2

            if diff > 3:
                is_safe = False

    return is_safe

total_safe = 0

with open("day2/input.txt") as input:
    for line in input.readlines():
        numlist = []
        for i in line.split(" "):
            numlist.append(int(i))

        is_first = True
        is_safe = True
        is_increasing = True
        dampened = False
        for i in range(len(numlist) - 1):
            num1 = numlist[i]
            num2 = numlist[i + 1]

            safe = check_vals(num1, num2, is_first, is_increasing)

            if not safe and not dampened:
                try:
                    new_check1 = check_vals(num1, numlist[i + 2], is_first, is_increasing)
                except:
                    new_check1 = False

                try:
                    new_check2 = check_vals(numlist[i - 1], num2, is_first, is_increasing)
                except:
                    new_check2 = False

                if new_check1 or new_check2:
                    safe = True
                    dampened = True

            if not safe:
                is_safe = False

        if is_safe:
            total_safe += 1


print(total_safe)

        