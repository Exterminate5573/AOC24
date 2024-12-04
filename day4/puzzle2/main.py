matrix = []

with open("day4/input.txt") as file:
    lines = file.readlines()
    for line in lines:
        a = []
        for letter in line:
            if letter == "\n": continue
            a.append(letter)
        matrix.append(a)

total = 0

for row in range(len(matrix)):
    for column in range(len(matrix[row])):
        c = str(matrix[row][column])

        if c == "A":
            if row - 1 < 0 or column - 1 < 0: continue
            try:
                topleft = matrix[row - 1][column - 1]
            except:
                continue
            try:
                topright = matrix[row + 1][column - 1]
            except:
                continue
            try:
                bottomleft = matrix[row - 1][column + 1]
            except:
                continue
            try:
                bottomright = matrix[row + 1][column + 1]
            except:
                continue
            if topleft == "M":
                if bottomright == "S":
                    if topright == "M":
                        if bottomleft == "S":
                            total += 1
                    if topright == "S":
                        if bottomleft == "M":
                            total += 1
            if topleft == "S":
                if bottomright == "M":
                    if topright == "M":
                        if bottomleft == "S":
                            total += 1
                    if topright == "S":
                        if bottomleft == "M":
                            total += 1

print(total)