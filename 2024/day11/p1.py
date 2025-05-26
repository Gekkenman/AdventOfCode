from math import ceil
with open("test.txt", "r") as f:
    data = f.read().strip().split(" ")

print(data)

f = open("out.txt", "w")
for _ in range(25):
    temp = []
    for i, stone in enumerate(data):
        if stone == "stop":
            continue
        if int(stone) == 0:
            temp.append('stop')
        elif len(stone) % 2 == 0:
            temp.append(stone[:ceil(len(stone) / 2)])
            x = stone[ceil(len(stone) / 2):]
            temp.append(str(int(x)) if int(x) != 0 else '0')
        else:
            temp.append(str(int(data[i]) * 2024))
    data = temp
    
    f.write(f"*{1 + _}*\n{data}\n")
    
f.close()
print(len(data))
