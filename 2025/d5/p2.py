def whereIsNum(low, high, num):
    if num < low:
        return "lower"
    elif num > high:
        return "higher"
    else:
        return "inside"

def main():
    with open("input.txt", "r") as f:
        fresh, ids = f.read().split("\n\n")
        fresh = [list(map(int, row.split("-"))) for row in fresh.strip().split("\n")]

        score = 0
        newFresh = []

        """
        Do the sort becouse of a edge case like this:
        15-18
        13-20
        10-14
        the code will make the following list [10-20, 15-18]
        """
        fresh.sort()

        for flow, fhigh in fresh:
            for i, num in enumerate(newFresh):

                nlow, nhigh = num
                posflow = whereIsNum(nlow, nhigh, flow)
                posfhigh = whereIsNum(nlow, nhigh, fhigh)

                if posflow == "inside" and posfhigh == "inside":
                    break
                elif posflow == "inside" and posfhigh == "higher":
                    newFresh[i] = [nlow, fhigh]
                    break
                elif posflow == "lower" and posfhigh == "inside":
                    newFresh[i] = [flow, nhigh]
                    break
            # fore else loop weared python Syntax
            else:
                newFresh.append([flow, fhigh])

        for low, high in newFresh:
            score += high - low + 1
        print(score)


if __name__ == "__main__":
    main()
