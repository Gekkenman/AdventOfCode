def main():
    with open("input.txt", "r") as f:
        IDs = list(map(lambda x: [int(x.split("-")[0]), int(x.split("-")[1])], f.read().strip().split(",")))

        score = 0
        for first, last in IDs:
            if len(str(first)) % 2 and len(str(last)) % 2:
                continue
            while first <= last:
                s = str(first)
                mid = len(s) // 2
                if s[:mid] == s[mid:]:
                    score += int(s)
                first += 1
        print(score)
    return


if __name__ == "__main__":
    main()
