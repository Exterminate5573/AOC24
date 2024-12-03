
list1 = []
list2 = []

with open("day1/input.txt") as input:
    for line in input.readlines():
        num1 = line.split("   ")[0]
        num2 = line.split("   ")[1]
        list1.append(int(num1))
        list2.append(int(num2))

list1.sort()
list2.sort()

total_dist = 0
for i in range(len(list1)):
    num1 = list1[i]
    num2 = list2[i]

    if num1 > num2:
        dist = num1 - num2
    else:
        dist = num2 - num1
    
    total_dist += dist

print(total_dist)