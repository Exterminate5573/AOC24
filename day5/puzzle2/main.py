from collections import defaultdict

dict = defaultdict(list)

with open("day5/input1.txt") as file:
    for line in file.readlines():
        str1, str2 = line.split("|")
        dict[int(str2)].append(int(str1))

total = 0

def sortlist(list):
    newlist = []

    for num in list:
        num = int(num)

        if len(newlist) == 0:
            newlist.append(num)
            continue

        test = None
    
        after = dict.get(num)
        for i in range(len(newlist)):
            num2 = newlist[i]
            before = dict.get(num2)

            if num2 in after:
                continue

            if num in before:
                test = i - 1
                if test == -1: test = 0
                break
        
        if test is not None:
            newlist.insert(test, num)
        else:
            newlist.append(num)

    return newlist


def bad_idea(numlist):
    run = True
    while run:
        fail = False
        for i in range(len(numlist)):
            num = int(numlist[i])

            tests = dict.get(num, None)
            if tests == None: continue

            for j in range(i+1, len(numlist)):
                check = int(numlist[j])
                if check in tests:
                    fail = True

        if fail:
            numlist = sortlist(numlist)
        else:
            run = False

    midpoint = (len(numlist) - 1) // 2
    mid = int(numlist[midpoint])
    return mid
        
with open("day5/input2.txt") as file:
    for line in file.readlines():
        numlist = line.strip().split(",")

        fail = False
        for i in range(len(numlist)):
            num = int(numlist[i])

            tests = dict.get(num, None)
            if tests == None: continue

            for j in range(i+1, len(numlist)):
                check = int(numlist[j])
                if check in tests:
                    fail = True

        if fail:
            total += bad_idea(numlist)

print(total)