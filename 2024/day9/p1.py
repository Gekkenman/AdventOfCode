with open("test.txt", "r") as f:
    data = list(map(int,list(f.read())))

t = []
y = 0
dots = 0
for i, num in enumerate(data):
    if i % 2:
        for _ in range(num):
            t.append(".")
        dots += num
    else:
        for _ in range(num):
            t.append(str(y))
        y += 1
print("".join(t))
a = []

for x in reversed(t):
    if x != ".":
        a.append(x)
        
out = []
z = 0
i = 0
while i < len(t) - dots:
    if t[i] == ".":
        out.append(a[z])
        z += 1
    else:
        out.append(t[i])
    i += 1

print("".join(out))

res = 0 
for i, num in enumerate(out):
    res += i * int(num)

print(res)