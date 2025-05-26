from itertools import product

l = []
with open("input.txt", "r") as f:
    for i, line in enumerate(f):
        l.append(line.strip().split(":"))
        l[i][1] = l[i][1].strip().split(" ")

for a in l:
    a[0] = int(a[0])
    a[1] = list(map(int, a[1]))


def getResults(l):
    res = []
    for option in product(list("+*|"), repeat=len(l) - 1):
        temp = l[0]
        for i, symbol in enumerate(option):
            if symbol == "*":
                temp *= l[i + 1]
            elif symbol == "+":
                temp += l[i + 1]
            else:
                temp = int(str(temp) + str(l[i + 1]))
        res.append(temp)
    return res

ans = 0
for operator in l:
    if operator[0] in getResults(operator[1]):
        ans += operator[0]
print(ans)