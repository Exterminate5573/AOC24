
map = []

with open("day6/input.txt") as file:
    lines = file.readlines()
    for line in lines:
        a = []
        for letter in line:
            if letter == "\n": continue
            a.append(letter)
        map.append(a)

#Very inefficient but effective!
#Could do it a better way but i have 32GB of ram so its not rlly an issue
running = True
while(running):
    for row in range(len(map)):
        columns = map[row]
        for column in range(len(columns)):
            pos = columns[column]

            match pos:
                case "^": dir = -1,0 ; next = ">"
                case "v": dir = 1,0 ; next = "<"
                case "<": dir = 0,-1 ; next = "^"
                case ">": dir = 0,1 ; next = "v"
                case _: continue

            if row + dir[0] < 1 or column + dir[0] < 1 or row + dir[0] > len(map) - 1 or column + dir[1] > len(columns) - 1:
                map[row][column] = "X"
                running = False
                break

            nextpos = map[row + dir[0]][column + dir[1]]
                
            if nextpos == "#":
                map[row][column] = next
            else:
                map[row + dir[0]][column + dir[1]] = pos
                map[row][column] = "X"

total = 0
for row in map:
    for column in row:
        if column == "X":
            total += 1

print(total)