def main():
    with open("example1.txt", "r") as f:
        score = 0
        cur = 50
        for line in f:
            rotation = line[:1]
            amount = int(line[1:].strip())

            if rotation == "L"



if __name__ == "__main__":
    main()
