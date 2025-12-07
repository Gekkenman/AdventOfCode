
def main():
    with open("input.txt", "r") as f:
        data = [[int(x)] for x in f.readline().strip().split()]
        for row in f.read().split("\n"):
            for i, unit in enumerate(row.split()):
                if unit not in "+*":
                    data[i].append(int(unit))
                else:
                    data[i].append(unit)

        score = 0
        for sum in data:
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
