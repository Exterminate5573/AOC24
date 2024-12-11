
stones = []

with open("day11/input.txt") as file:
    line = file.readline()
    nums = line.split(" ")
    for num in nums:
        num = int(num)
        stones.append(num)

for _ in range(25):
    for i in range(len(stones)):
        num = stones[i]

        if num == 0:
            stones[i] = 1
            continue

        text = str(num)
        if len(text) % 2 == 0:
            size = int(len(text) / 2)

            first = text[0:size]
            last = text[size:]

            stones[i] = int(first)
            stones.append(int(last))
            continue
            
        stones[i] = num * 2024
            
print(len(stones))