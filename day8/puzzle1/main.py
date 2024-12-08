from collections import defaultdict

map = defaultdict(list)

with open("day8/input.txt") as file:
    lines = file.readlines()
    for l in range(len(lines)):
        line = lines[l]
        for t in range(len(line)):
            text = line[t]

            if text != "." and text != "\n":
                map[text].append((t,l))

outcoords = []

for id in map:
    coords = map[id]
    for i in range(len(coords)):
        coord = coords[i]
        for j in range(i+1, len(coords)):
            coord2 = coords[j]
            if coord == coord2: continue

            x1 = coord[0]
            y1 = coord[1]
            x2 = coord2[0]
            y2 = coord2[1]
            
            try:
                diff = (y2 - y1) / (x2 - x1)
            except:
                continue
                #diff = y2 - y1

            print(abs(diff))

            if diff % 1 == 0:
                #print(coord, coord2)
                newcoord1 = (x1 - diff, y1 - diff)
                newcoord2 = (x2 + diff, y2 + diff)

                #if newcoord1[0] > 49 or newcoord1[1] > 49 or newcoord2[0] > 49 or newcoord2[1] > 49: continue
                if newcoord1[0] > 11 or newcoord1[1] > 11 or newcoord2[0] > 11 or newcoord2[1] > 11: continue
                if newcoord1[0] < 0 or newcoord1[1] < 0 or newcoord2[0] < 0 or newcoord2[1] < 0: continue

                outcoords.append(newcoord1)
                outcoords.append(newcoord2)

print(len(outcoords))