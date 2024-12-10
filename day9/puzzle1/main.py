
line = ""
with open("day9/input.txt") as file:
    line = file.readline()

c = 0
id = 0
files = []
for num in line:
    num = int(num)

    if c % 2 == 0:
        #File
        for i in range(num):
            files.append(id)

        id += 1
    else:
        #Free space
        for i in range(num):
            files.append(-1)

    c += 1

while -1 in files:
    num = files.pop()

    if num == -1:
        continue

    i = files.index(-1)
    files[i] = num

total = 0

i = 0
for j in files:
    total += i * j

    i += 1

print(total)