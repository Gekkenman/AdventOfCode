with open("input.txt", "r") as f:
    data = f.read().strip()

val = []

for i, c in enumerate(data):
    if int(c) == 0:
        continue
    if not i % 2:
        val.append((int(c), i // 2))
    else:
        val.append((int(c), "."))

ans = []
while val:
    v = val.pop(0)
        
    if v[1] == ".":
        # from this:
        # [(2, 0), (3, "."), ....... (2, 9)]
        # to this:
        # [(2, 9), (1, "."), ....... (2, "swaped")]
        for i, d in enumerate(reversed(val)):
            index = len(val) - i - 1
            if d[1] == "." or d[1] == "swaped":
                continue
            if d[0] < v[0]:
                val[index] = (d[0], "swaped")
                val.insert(0, (v[0] - d[0], "."))
                val.insert(0, d)
                break
            elif d[0] == v[0]:
                val[index] = (v[0], "swaped")
                val.insert(0, d)
                break
        else:
            # when the loop ends en there was no sawp posible replace the "." with "swaped"
            if v[1] == ".":
                val.insert(0, (v[0], "swaped"))
    else:
        ans.extend([v[1]] * v[0])

out = 0

for i in range(len(ans)):
    if ans[i] == "swaped":
        ans[i] = "."
    else:
        out += ans[i] * i
        ans[i] = str(ans[i])

print(out)