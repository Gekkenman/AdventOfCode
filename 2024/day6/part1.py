answer = 0
grid = []
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
with open("input.txt", "r") as f:
    for y, line in enumerate(f):
        grid.append([])
        for x, char in enumerate(line.strip()):
            grid[y].append(char)
            if char == "^":
                start = (y, x)

y, x = start
directionCounter = 0
while True:
    
    if grid[y][x]:
        answer += 1

    grid[y][x] = False
    dy = y + direction[directionCounter][0]
    dx = x + direction[directionCounter][1]

    if dy >= len(grid) or dy < 0 or dx >= len(grid[0]) or dx < 0:
        break
    if grid[dy][dx] == "#":
        directionCounter = (directionCounter + 1) % 4
    y += direction[directionCounter][0]
    x += direction[directionCounter][1]
print(answer)

