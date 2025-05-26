with open("input.txt", "r") as f:
    data = list(f.read().strip().split())

seen = []
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
ans = 0
def isInBound(y, x):
    if y < 0 or y >= len(data) or x < 0 or x >= len(data):
        return False
    return True

def dsf(y, x, group, seen, i):
    seen.append((y, x))
    notVisited.remove((y, x))
    d[i]["groupSize"] += 1
    for Y, X in moves:
        dy = y + Y
        dx = x + X
        if isInBound(dy, dx) and data[dy][dx] == group:
            if (dy, dx) not in seen:
                dsf(dy, dx, group, seen, i)
        else:
            d[i][(Y, X)].append((dy, dx))

notVisited = set()
for y in range(len(data)):
    for x in range(len(data[y])):
        notVisited.add((y, x))

i = 0
d = {}
while notVisited:
    y, x = list(notVisited)[0]
    d[i] = {
        "groupSize": 0,
        (-1, 0): [],
        (1, 0): [],
        (0, -1): [],
        (0, 1): []
    }
    dsf(y, x, data[y][x], [], i)
    i += 1

def dfs2(y, x, seen, key, move):
    seen.append((y, x))
    for Y, X in moves:
        dy = y + Y
        dx = x + X
        if (dy, dx) in d[key][move]:
            d[key][move].remove((dy, dx))
            dfs2(dy, dx, seen, key, move)

ans = 0
for key in d:
    fence = 0
    for move in moves:
        while d[key][move]:
            y, x = d[key][move].pop()
            dfs2(y, x, [], key, move)
            fence += 1
    ans += fence * d[key]["groupSize"]

print(ans)