
matrix = []

with open("day10/input.txt") as file:
    lines = file.readlines()
    for line in lines:
        a = []
        for letter in line:
            if letter == "\n": continue
            a.append(int(letter))
        matrix.append(a)

total = 0

reached_spots = []

def checknext(num, row, column):
    if row < 0 or column < 0: return

    try:
        current = matrix[row][column]
    except:
        return
    
    if current == num:

        if num == 9:
            if not (row,column) in reached_spots:
                global total
                total += 1
                
                reached_spots.append((row,column))

            return

        for coord in [(1,0),(-1,0),(0,1),(0,-1)]:
            x = coord[0]
            y = coord[1]

            checknext(num+1, row + x, column + y)

for row in range(len(matrix)):
    for column in range(len(matrix[row])):
        checknext(0, row, column)
        reached_spots = []

print(total)