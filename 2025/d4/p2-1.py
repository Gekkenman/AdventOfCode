def main():
    with open("input.txt", "r") as f:
        rolls = set()
        for y, row in enumerate(f):
            for x, char in enumerate(row.strip()):
                if char == "@":
                    rolls.add((y, x))
        removeRolls = set()
        adj = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]
        score = 0
        while True:
            for roll in removeRolls:
                rolls.remove(roll)
            removeRolls.clear()

            for y, x in rolls:
                counter = 0
                for dy, dx in adj:
                    if (y + dy, x + dx) in rolls:
                        counter += 1
                if counter < 4:
                    removeRolls.add((y, x))
                    score += 1
            if len(removeRolls) == 0:
                break
        print(score)


if __name__ == "__main__":
    main()
