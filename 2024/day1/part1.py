row1 = []
row2 = []
with open("input.txt", "r") as f:
    for line in f:
        line = line.split()
        row1.append(int(line[0]))
        row2.append(int(line[1]))
row1.sort()
row2.sort()
result = 0 
for r1, r2 in zip(row1, row2):
   result += abs(r2 - r1)
print(result) 
