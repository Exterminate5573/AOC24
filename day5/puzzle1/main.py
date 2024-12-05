from collections import defaultdict

dict = defaultdict(list)

with open("day5/input1.txt") as file:
    for line in file.readlines():
        str1, str2 = line.split("|")
        dict[int(str2)].append(int(str1))

total = 0

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

        if not fail:
            midpoint = (len(numlist) - 1) // 2
            mid = int(numlist[midpoint])
            total += mid

print(total)