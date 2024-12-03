
list1 = []
list2 = []

with open("day1/input.txt") as input:
    for line in input.readlines():
        num1 = line.split("   ")[0]
        num2 = line.split("   ")[1]
        list1.append(int(num1))
        list2.append(int(num2))


total_sim = 0

for i in list1:
    num2 = list2.count(i)

    sim = i * num2

    total_sim += sim

print(total_sim)