import re

with open("test.txt", "r") as f:
    s = f.read()
    temp = list(map(int,re.findall(r"\d+", s)))
    data = {}
    i = 0
    for _ in range(len(temp) // 6):
        data[i] = {
            "A":(temp[i], temp[i + 1]),
            "B":(temp[i + 2], temp[i + 3]),
            "P":(10000000000000 + temp[i + 4], 10000000000000 + temp[i + 5])
        }
        i += 6

ans = 0
for key in data:
    ax, ay = data[key]["A"]
    bx, by = data[key]["B"]
    px, py = data[key]["P"]
    aPress = 0
    while aPress < 1000:
        x = (px - (aPress * ax)) / bx
        y = (py - (aPress * ay)) / by
        print(x, y)
        if x.is_integer() and y.is_integer() and x == y:
            print(x, y)
            ans += int(aPress * 3 + x)
            break
        aPress += 1

        
print(ans)