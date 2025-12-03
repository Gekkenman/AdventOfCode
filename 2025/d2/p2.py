def main():
    with open("input.txt", "r") as f:
        # create list of id's that is like [[123, 123]]
        IDs = list(map(lambda x: [int(x.split("-")[0]), int(x.split("-")[1])], f.read().strip().split(",")))

        score = 0
        for first, last in IDs:

            # check all the id's between and including the first land last
            while first <= last:
                s = str(first)
                num = 1

                # check all repeated sequence of numbers that are posible.
                # this can be at most up to and including half of the digits of the id.
                # example "123123123123123" has 15 digits the posible repeated sequence can be 1, 3, 5 long
                while num <= len(s) // 2:
                    check = len(s) / num
                    if not check % 1:
                        begin = 0
                        end = num
                        valid = False

                        # check if ther is a repeating structure and if not set valid to True
                        for _ in range(len(s) // num - 1):
                            if s[begin:end] != s[begin + num:end + num]:
                                valid = True
                            begin += num
                            end += num
                        if not valid:
                            score += int(s)
                            break
                    num += 1
                first += 1
        print(score)
    return


if __name__ == "__main__":
    main()
