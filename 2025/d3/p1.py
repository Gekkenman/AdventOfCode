def main():
    with open("input.txt", "r") as f:
        batteries = f.read().strip().split("\n")
        ans = 0
        for batterie in batteries:
            bigest = 0
            secondBigest = 0
            for i, num in enumerate(list(map(int, batterie))):
                if num > bigest and len(batterie) - 1 != i:
                    bigest = num
                    secondBigest = 0
                elif num > secondBigest:
                    secondBigest = num
            print(bigest, secondBigest)
            ans += bigest * 10 + secondBigest
        print(ans)

    pass

if __name__ == "__main__":
    main()
