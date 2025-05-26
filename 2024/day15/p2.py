import re

directions = {
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1)
}

def main():
    grid, y, x, moves = getData()
    for move in moves:
        grid[y][x] = "."
        Y, X = directions[move]
        dy = y + Y
        dx = x + X
        next = grid[dy][dx]
        if Y == -1 or Y == 1:
            boxes, spaces = dfs(grid, dy, dx, Y, set(), set())
            boxes = list(boxes)
            if Y == -1:
                boxes.sort()
            else:
                boxes.sort(reverse=True)

            if boxes:
                push = True
                for space in spaces:
                    if grid[space[0]][space[1]] == "#":
                        push = False
                        break
                if push:
                    for box in boxes:
                        grid[box[0] + Y][box[1]] = grid[box[0]][box[1]]
                        grid[box[0]][box[1]] = "."
                    y += Y
            else:
                dy, dx = spaces.pop()
                if grid[dy][dx] != "#":
                    y = dy
                    x = dx
        else:
            stack = [next]
            while next in "[]":
                dy += Y
                dx += X
                next = grid[dy][dx]
                stack.append(next)

            if stack.pop() == ".":
                for _ in range(len(stack)):
                        grid[dy][dx] = stack.pop()
                        dy -= Y
                        dx -= X
                y = dy
                x = dx
        grid[y][x] = "@"
    printGrid(grid)

    ans = 0
    for y in range(len(grid)):
        for x  in range(len(grid[y])):
            if grid[y][x] == "[":
                ans += 100 * y + x
    print(ans)
    return 0

def dfs(grid, y, x, Y, boxes, space):
    curr = grid[y][x]
    if curr not in "[]":
        space.add((y, x))
    elif curr == "[":
        boxes.add((y, x))
        boxes.add((y, x + 1))
        newB, newX = dfs(grid, y + Y, x, Y, set(), set())
        boxes.update(newB)
        space.update(newX)
        newB, newX = dfs(grid, y + Y, x + 1, Y, set(), set())
        boxes.update(newB)
        space.update(newX)
    elif curr == "]":
        boxes.add((y, x))
        boxes.add((y, x - 1))
        newB, newX = dfs(grid, y + Y, x, Y, set(), set())
        boxes.update(newB)
        space.update(newX)
        newB, newX = dfs(grid, y + Y, x - 1, Y, set(), set())
        boxes.update(newB)
        space.update(newX)
    return boxes, space

def getData():
    grid = []
    with open("input.txt", "r") as f:
        gd, md = f.read().split("\n\n")

    for i, line in enumerate(gd.split("\n")):
        line = line.strip()
        grid.append([])
        for p, char in enumerate(line):
            if char == "O":
                grid[i].append("[")
                grid[i].append("]")
            elif char == "@":
                y = i
                x = p * 2
                grid[i].append("@")
                grid[i].append(".")
            else:
                grid[i].append(char)
                grid[i].append(char)
    
    return grid, y, x, md.replace("\n", "").strip()

def printGrid(grid):
    out = ""
    for row in grid:
        out += "".join(row) + "\n"
    print(out)
        






if __name__ == "__main__":
    main()