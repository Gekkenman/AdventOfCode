def main():
    result = 0
    result2 = 0
    rules = {}
    updates = []
    with open("input.txt", "r") as f:
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

    # this code is shit but it works 
    for update in updates:
        if isUpdateCorrect(update, rules):
            result += update[(len(update) - 1) // 2]
        else:
            result2 += fixUpdate(update, rules)[(len(update) - 1) // 2]
    
    print(result)
    print(result2)
                    
def isUpdateCorrect(update, rules):
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
        return safe

def fixUpdate(update, rules):
    #Base case update is correct
    if isUpdateCorrect(update, rules):
        return update
    
    for i, num in enumerate(update):
        left = update[:i]
        right = update[i:]
        if left and num in rules.keys():
            for y, n in enumerate(left):
                if n in rules[num]:
                    update[i] = n
                    update[y] = num
                    print(update)
                    return fixUpdate(update, rules)
        if right:
            for y, n in enumerate(right[1:]):
                if n in rules.keys() and num in rules[n]:
                    update[i] = n
                    update[y + i + 1] = num
                    return fixUpdate(update, rules)



if __name__ == "__main__":
    main()