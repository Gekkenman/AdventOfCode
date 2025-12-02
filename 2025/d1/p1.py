def main():
    with open("input.txt", "r") as f:
        score = 0
        cur = 50
        for line in f:
            rotation = line[:1]
            amount = int(line[1:].strip())
            if rotation == "L":
                cur = (cur - amount) % 100
            else:
                cur = (cur + amount) % 100
            if cur == 0:
                score += 1
        print(score)
    return


if __name__ == "__main__":
    main()
