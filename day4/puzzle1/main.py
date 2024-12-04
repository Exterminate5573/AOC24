
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

        if c == "X":
            for i in [-1,0,1]:
                for j in [-1,0,1]:
                    if i == 0 and j == 0: continue
                    if row + i + i + i < 0 or column + j + j + j < 0: continue
                    try:
                        letter = matrix[row + i][column + j]
                    except:
                        continue
                    if letter == "M":
                        try:
                            letter2 = matrix[row + i + i][column + j + j]
                        except:
                            continue
                        if letter2 == "A":
                            try:
                                letter3 = matrix[row + i + i + i][column + j + j + j]
                            except:
                                continue
                            if letter3 == "S":
                                total += 1

print(total)