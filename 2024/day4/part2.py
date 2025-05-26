offsets = [(-1, -1), (1, 1), (-1, 1), (1, -1)]
grid = []

def main():
    answer = 0
    # load data struct
    with open("input.txt", "r") as f:
        for line in f:
            grid.append(list(line.strip()))

    # loop over grid
    for y in range(1, len(grid) - 1):
        for x in range(1, len(grid[0]) - 1):
            if grid[y][x] == "A":
                answer += checkXmas(y, x)
    print(answer)

def checkXmas(y, x):
    chars = []
    for offset in offsets:
        char = grid[y + offset[0]][x + offset[1]]
        if char != "M" and char != "S":
            return 0
        chars.append(char)
    
    if chars[0] != chars[1] and chars[2] != chars[3]:
        return 1
    else:
        return 0

if __name__ == "__main__":
    main()