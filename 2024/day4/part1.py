target = "XMAS"
offsets = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 1),
    (1, -1), (1, 0), (1, 1)
]
grid = []

def main():
    answer = 0
    # load data struct
    with open("input.txt", "r") as f:
        for line in f:
            grid.append(list(line.strip()))

    # loop over grid
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            
            # start search when there is a match with the first char
            if grid[y][x] == target[0]:
                answer += findXmas(y, x)
    print(answer)

def findXmas(y, x):
    found = 0
    for offset in offsets:
        newY = y + offset[0]
        newX = x + offset[1]
        xmas = False
        if checkIndex(newY, newX):
            for char in target[1:]:
                if checkIndex(newY, newX):
                    if grid[newY][newX] == char:
                        newY += offset[0]
                        newX += offset[1]
                        if char == target[-1]:
                            xmas = True
                    else:
                        xmas = False
                        break
            if xmas:
                found += 1
    return found


def checkIndex(y, x):
        if y > -1 and y < len(grid) and x > -1 and x < len(grid[0]):
            return 1
        else:
            return 0


if __name__ == "__main__":
    main()