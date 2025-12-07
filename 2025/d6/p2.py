
def main():
    with open("input.txt", "r") as f:
        grid = [list(row) for row in f.read().split("\n")]
        grid.pop()
        f.seek(0)
        sums = [[] for _ in range(len(f.readline().strip().split()))]
        counter = 0
        for x in range(len(grid[0])):
            x = len(grid[0]) - 1 - x
            num = ""
            for y in range(len(grid)):
                if grid[y][x].isdigit():
                    num += grid[y][x]
                elif grid[y][x] in "+*":
                    sums[counter].append(int(num))
                    sums[counter].append(grid[y][x])
                    counter += 1
                    num = ""
            if num:
                sums[counter].append(int(num))

        score = 0
        for sum in sums:
            temp = 0
            operation = sum.pop()
            if operation == "+":
                for num in sum:
                    temp += num
            else:
                temp = 1
                for num in sum:
                    temp *= num
            score += temp
        print(score)


if __name__ == "__main__":
    main()
