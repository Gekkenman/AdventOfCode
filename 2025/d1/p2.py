def main():
    with open("input.txt", "r") as f:
        score = 0
        cur = 50
        skip = False
        for line in f:
            rotation = line[:1]
            amount = int(line[1:].strip())
            score += amount // 100
            amount %= 100
            if cur == 0:
                skip = True
            if rotation == "L":
                cur -= amount
            elif rotation == "R":
                cur += amount
            if not skip and cur != cur % 100 or cur == 0:
                score += 1
            else:
                skip = False
            cur = cur % 100
        print(score)
    return


if __name__ == "__main__":
    main()
