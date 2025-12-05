def main():
    with open("input.txt", "r") as f:
        fresh, ids = f.read().split("\n\n")
        fresh = [list(map(int, row.split("-"))) for row in fresh.strip().split("\n")]
        ids = list(map(int, ids.strip().split("\n")))

        score = 0
        for id in ids:
            for low, high in fresh:
                if low <= id <= high:
                    #print(f"{low} >= {id} <= {high} = true")
                    score += 1

                    break
        print(score)


if __name__ == "__main__":
    main()
