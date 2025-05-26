from itertools import combinations

grid = []
with open("input.txt", "r") as f:
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
def getSpots(start, offset):
    y, x = start
    dy, dx = offset
    ret = set()
    while isInBound((y, x)):
        ret.add((y, x))
        y += dy
        x += dx
    return ret

ans = set()
for key in d:
    spots = set()
    for pair in combinations(d[key], 2):
        offset = tuple(map(lambda pair: pair[0] - pair[1], zip(pair[0], pair[1])))
        spots = spots.union(getSpots(pair[0], offset))
        spots = spots.union(getSpots(pair[1], (offset[0] * -1, offset[1] * -1)))
    ans = ans.union(list(spots))
print(len(ans))