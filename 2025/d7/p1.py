def main():
    with open("input.txt", "r") as f:
        grid = list(map(list, f.read().strip().split("\n")))

        for y, row in enumerate(grid):
            for x, char in enumerate(row):
                if char == "S":
                    start = (y, x)
                    break
                else:
                    continue
                break

    q = set()
    q.add(start)
    seen = []
    score = 0

    while q:
        y, x = q.pop()
        dy = y + 1
        if dy >= len(grid) or (dy, x) in seen:
            continue
        elif grid[dy][x] == "^":
            q.add((dy, x + 1))
            q.add((dy, x - 1))
            seen.append((dy, x))
            score += 1
        else:
            q.add((dy, x))

    print(score)




if __name__ == "__main__":
    main()
