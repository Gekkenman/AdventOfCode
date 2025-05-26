from itertools import combinations

grid = []
with open("example.txt", "r") as f:
    for line in f:
        grid.append(list(line.strip()))

d = {}
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] != "." and grid[y][x] in d.keys():
            d[grid[y][x]] += [(y, x)]
        elif grid[y][x] != ".":
            d[grid[y][x]] = [(y, x)]

def isInBound(cords):
    y, x = cords
    if y < 0 or y >= len(grid) or x < 0 or x >= len(grid[0]):
        False
    else:
        return True

ans = 0
spots = set()
for key in d:
    for pair in combinations(d[key], 2):
        offset = tuple(map(lambda pair: pair[0] - pair[1], zip(pair[0], pair[1])))
        hot1 = (pair[0][0] + offset[0], pair[0][1] + offset[1])
        hot2 = (pair[1][0] - offset[0], pair[1][1] - offset[1])
        #print(f"pair: {pair}, offset: {offset}, hot1: {hot1}, hot2: {hot2}")
        if isInBound(hot1):
            spots.add(hot1)
        if isInBound(hot2):
            spots.add(hot2)

for y,x in spots:
    grid[y][x] = "@"
for row in grid:
    print("".join(row))
print(len(spots))