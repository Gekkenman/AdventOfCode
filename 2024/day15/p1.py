import re


def getData():
    with open("input.txt", "r") as f:
        data = f.read()
        temp, moves = data.split("\n\n")
    grid = []

    for line in temp.split("\n"):
        grid.append(list(line.strip()))
    start = ()
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "@":
                start = (y, x)
                break
        if start:
            break
    
    return grid, start, moves.replace("\n", "")

def printGrid():
    out = ""
    for row in grid:
        out += "".join(row) + "\n"
    print(out)

def getMoves():
    global moves
    if not moves:
        return 0
    char = re.search(r"(.)\1*", moves)[0]
    moves = moves[len(char):]
    y = directions[char[0]][0]
    x = directions[char[0]][1]
    return (len(char), y, x)


grid, start, moves = getData()

directions = {
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1)
}
while moves:
    steps, Y, X = getMoves()
    stack = ["@"]
    grid[start[0]][start[1]] = "."
    dy = start[0]
    dx = start[1]
    next = grid[start[0]][start[1]]
    i = 0
    while i < steps:
        dy += Y
        dx += X
        i += 1
        next = grid[dy][dx]
        if next == "#":
            stack.append(((dy - Y), (dx - X)))
            break
        elif next == "O":
            grid[dy][dx] = "."
            i -= 1
            stack.append("O")
        elif i >= steps:
            stack.append((dy, dx))

    start = stack.pop()
    while stack:
        char = stack.pop()
        grid[start[0]][start[1]] = char
        start = (start[0] - Y, start[1] - X)
    start = (start[0] + Y, start[1] + X)

ans = 0
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == "O":
            ans += y * 100 + x

printGrid()
print(ans)