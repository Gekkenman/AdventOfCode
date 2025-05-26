row1 = {}
row2 = {} 
with open("input.txt", "r") as f:
    for line in f:
        x, y = line.split()
        if x in row1.keys():
            row1[x] += int(x)
        else:
            row1[x] = int(x)
        if y in row2.keys():
            row2[y] += 1
        else:
            row2[y] = 1

answer = 0
for key in row1.keys():
    if key in row2.keys():
        answer += row1[key] * row2[key]

print(answer)
