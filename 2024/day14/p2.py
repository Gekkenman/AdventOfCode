import re
from copy import deepcopy

with open("input.txt", "r") as f:
    data = []
    for line in f:
        line = line.strip()
        data.append(tuple(map(int, re.findall(r"-?\d+", line))))

width = 101
hight = 103
#px, py, vx, vy = data[0]
def makeGrid():
    return [["." for _ in range(width)] for x in range(hight)]
    
def gprint(grid):
    out = ""
    for line in grid:
        out += "".join(line)
        out += "\n"
    return out

directions = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1), (0, 1),
              (1, -1), (1, 0), (1, 1)]

def dfs(point, visited):
    stack = [point]
    size = 0
    while stack:
        y, x = stack.pop()
        if (y, x) in visited:
            continue
        visited.add((y,x))
        size += 1
        for Y, X in directions:
            neighbor = (y + Y, x + X)
            if neighbor in temp and neighbor not in visited:
                temp.remove(neighbor)
                stack.append(neighbor)
    return size

f = open("out.txt", "w")
i = 0
bigest = [-1, i, []]
while i < 10000:
    visited = set()
    out = set()
    for px, py, vx, vy in data:
        newx = (vx * i+ px) % width
        newy = (vy * i+ py) % hight
        out.add((newy, newx))
    temp = list(deepcopy(out))
    while temp:

        size = max(bigest[0], dfs(temp.pop(), set()))
        if size > bigest[0]:
            bigest = [size, i, out]
    i += 1

grid = makeGrid()
for y, x in bigest[2]:
    grid[y][x] = "#"
wr = f"Seconds: {bigest[1]} Size: {bigest[0]}\n"
wr += gprint(grid)
f.write(wr)
f.close()