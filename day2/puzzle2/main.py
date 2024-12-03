#Incomplete
total_safe = 0

with open("day2/input.txt") as input:
    for line in input.readlines():
        numlist = []
        for i in line.split(" "):
            numlist.append(int(i))

        dampened = False
        is_first = True
        is_safe = True
        is_increasing = True
        curr_num = numlist.pop()
        while len(numlist) > 0:
            num1 = curr_num
            num2 = numlist.pop()

            if is_first:
                if num1 < num2:
                    is_increasing = True
                elif num1 > num2:
                    is_increasing = False
                else:
                    if not dampened:
                        curr_num = num2
                        dampened = True
                        continue
                    else:
                        is_safe = False
                        break

                is_first = False

            if is_increasing:
                if num1 >= num2:
                    if not dampened:
                        curr_num = num2
                        dampened = True
                        continue
                    else:
                        is_safe = False
                        break
                else:
                    diff = num2 - num1

                    if diff > 3:
                        if not dampened:
                            curr_num = num2
                            dampened = True
                            continue
                        else:
                            is_safe = False
                            break
            else:
                if num1 <= num2:
                    if not dampened:
                        curr_num = num2
                        dampened = True
                        continue
                    else:
                        is_safe = False
                        break
                else:
                    diff = num1 - num2

                    if diff > 3:
                        if not dampened:
                            curr_num = num2
                            dampened = True
                            continue
                        else:
                            is_safe = False
                            break
            
            curr_num = num2
        
        if is_safe:
            total_safe += 1


print(total_safe)