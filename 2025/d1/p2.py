def main():
    with open("example1.txt", "r") as f:
        score = 0
        cur = 50
        for line in f:
            rotation = line[:1]
            amount = int(line[1:].strip())
            score += amount // 100
            amount %= 100

            # print(f"{cur} Score: {score}")
            if rotation == "L":
                print(f"From: {cur} - {amount} = ", end="")
                cur -= amount
                print(cur % 100, end="")
            elif rotation == "R":
                print(f"From: {cur} + {amount} = ", end="")
                cur += amount
                print(cur % 100, end="")
            if cur != cur % 100:
                score += 1
                print(" Score: +1")
            else:
                print()
            cur = cur % 100
        print(score)
    return


if __name__ == "__main__":
    main()
