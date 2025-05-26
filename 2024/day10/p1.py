with open("input.txt", "r") as f:
    data = []
    for line in f:
        data.append(list(map(int, list(line.strip()))))

direcionts = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(height, y, x):
    out = set()
    if height == 9:
        return {(y, x)}
    else:
        for Y, X in direcionts:
            dy = y + Y
            dx = x + X
            if dy >= len(data) or dy < 0 or dx >= len(data[0]) or dx < 0:
                continue
            elif data[dy][dx] == height + 1:
                temp = dfs(height + 1, dy, dx)
                out.update(temp)
        return out
ans = 0
for y in range(len(data)):
    for x in range(len(data[0])):
        if data[y][x] == 0:
            ans += len(dfs(0, y, x))

print(ans)