import copy

def main():
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

    path = getPath(start, copy.deepcopy(grid), direction)
    path.reverse()
    for cell in path:
        if isLoop(start, copy.deepcopy(grid), cell, direction):
            answer += 1
    print(answer)

def isLoop(start, grid, cell, direction):
    buffer = []
    d = {}
    offset = 1
    firstOfCycle = None
    grid[cell[0]][cell[1]] = "#"
    y, x = start
    directionCounter = 0
    while True:
        dy = y + direction[directionCounter][0]
        dx = x + direction[directionCounter][1]

        if dy >= len(grid) or dy < 0 or dx >= len(grid[0]) or dx < 0:
            return False
        
        if grid[dy][dx] == "#":
            directionCounter = (directionCounter + 1) % 4
            ddy = y + direction[directionCounter][0]
            ddx = x + direction[directionCounter][1]
            if (ddy >= len(grid) or ddy < 0 or ddx >= len(grid[0]) or ddx < 0) or grid[ddy][ddx] == "#":
                directionCounter = (directionCounter + 1) % 4
            
            new = (dy, dx)
            if firstOfCycle:
                if len(d[firstOfCycle]) > 1:
                    for index in d[firstOfCycle][:1]:
                        if buffer[index + offset] and buffer[index + offset] == firstOfCycle:
                            return True
                        elif buffer[index + offset] == new:
                            offset += 1
                            addKey(d, new, len(buffer))
                        else:
                            firstOfCycle = new
                            addKey(d, new, len(buffer))
                else:
                    firstOfCycle = new
                    addKey(d, new, len(buffer))
            else:
                firstOfCycle = new
                addKey(d, new, len(buffer))
            buffer.append(new)
        
        y += direction[directionCounter][0]
        x += direction[directionCounter][1]
        

def addKey(d, new, index):
    if new in d.keys():
        d[new].append(index)
    else:
        d[new] = [index]




def getPath(start, grid, direction):
    y, x = start
    directionCounter = 0
    path = []
    while True:
        if grid[y][x]:
            path.append((y, x))

        grid[y][x] = False

        dy = y + direction[directionCounter][0]
        dx = x + direction[directionCounter][1]

        if dy >= len(grid) or dy < 0 or dx >= len(grid[0]) or dx < 0:
            break

        if grid[dy][dx] == "#":
            directionCounter = (directionCounter + 1) % 4

        y += direction[directionCounter][0]
        x += direction[directionCounter][1]
    return path


if __name__ == "__main__":
    main()