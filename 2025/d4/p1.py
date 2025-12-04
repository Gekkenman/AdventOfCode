

def main():
    with open("input.txt", "r") as f:
        grid =  list(map(list, f.read().strip().split("\n")))
        adj = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]
        score = 0
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                counter = 0
                if grid[y][x] != "@":
                    continue
                for dy, dx in adj:
                    if y + dy < 0 or y + dy > len(grid) - 1 or x + dx < 0 or x + dx > len(grid[y]) - 1:
                        continue
                    elif grid[y + dy][x + dx] == "@":
                        counter += 1
                if counter < 4:
                    score += 1
        print(score)


if __name__ == "__main__":
    main()
