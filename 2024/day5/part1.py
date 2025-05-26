def main():
    result = 0
    rules = {}
    updates = []
    with open("example.txt", "r") as f:
        flag = True
        for line in f:
            line = line.strip()
            if line == "":
                flag = False
                continue
            if flag:
                x, y = line.split("|")
                x = int(x)
                y = int(y)
                if x in rules.keys():
                    rules[x].append(y)
                else:
                    rules[x] = [y]
            else:
                updates.append(list(map(int, line.split(","))))

    keys = rules.keys()
    for key in keys:
        print(f"key: {key} list: {rules[key]}")

    # this code is shit but it works 
    for update in updates:
        safe = True
        for i, num in enumerate(update):
            left = update[:i]
            right = update[i:]
            if left and num in rules.keys():
                for n in left:
                    if n in rules[num]:
                        safe = False
            if right:
                for n in right:
                    if n in rules.keys() and num in rules[n]:
                        safe = False
        if safe:
            result += update[(len(update) - 1) // 2]
    
    print(result)
                    


if __name__ == "__main__":
    main()