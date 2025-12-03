def main():
    with open("input.txt", "r") as f:
        batteries = f.read().strip().split("\n")
        ans = 0
        size = 12
        for batterie in batteries:
            bsize = len(batterie)
            bigest = [0] * size
            for i, num in enumerate(list(map(int, batterie))):
                clear = False
                for j in range(size):
                    if clear:
                        bigest[j] = 0
                    elif num > bigest[j] and bsize - i >= size - j:
                        bigest[j] = num
                        clear = True
            for i, num in enumerate(bigest):
                ans += pow(10, size - i - 1) * num
        print(ans)

    pass


if __name__ == "__main__":
    main()
