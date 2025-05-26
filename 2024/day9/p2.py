#with open("example.txt", "r") as f:
    #data = f.read()
data = "2333133121414131402"
dots = []
val = []

for i, c in enumerate(data):
    if not i % 2:
        val.append((int(c), i // 2))
    else:
        dots.append(int(c))
ans = []
print(dots)
print(val)
d = 0
l =  len(val) - 1
i = 0
even = True
while val:
    if even:
        v = val.pop(0)
        ans.extend([v[1]] * v[0])
    else:
        n = len(val) - 1
        for y, v in enumerate(reversed(val)):
            if v[0] < dots[d]:
                ans.extend([v[1]] * v[0])
                dots[d] -= v[0]
                val.pop(n - y)
            elif v[0] == dots[d]:
                ans.extend([v[1]] * v[0])
                val.pop(n - y)
                dots[d] -= v[0]
                break
        if dots[d] != 0:
            ans.extend([0] * dots[d])
        d += 1
    even = not even
out = 0
print("".join(list(map(str, ans))))
for i, num in enumerate(ans):
    out += i * num
print(out)