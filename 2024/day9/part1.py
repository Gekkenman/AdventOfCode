with open("input.txt", "r") as f:
    data = f.read()
file = []

if len(data) % 2 == 0:
    # even means last digit is for free space so we can skip it
    index = len(data) - 2
    k = len(data) - 1
    valLast = len(data) // 2 -1
else:
    index = len(data) - 1
    k = len(data)
    valLast = len(data) // 2
dataCout = 0

i = 0
while i < k:
    if i % 2:
        # how mutch space is ther in the free space
        space = int(data[i])
        while space > 0:
            # how big is the data at the end
            end = int(data[index])
            if end <= space:
                file.extend([valLast] * end)
                space -= end
                valLast -= 1
                index -= 2
                k -= 2
            else:
                file.extend([valLast] * space)
                data = data[:index] + str(end - space)
                break
    else:
        file.extend([dataCout] * int(data[i])) 
        dataCout += 1
    i += 1

ans = 0
for i, num in enumerate(file):
    ans += i * num
print(ans)