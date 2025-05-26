with open("example.txt", "r") as f:
    data = list(f.read().strip().split())

seen = []
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
ans = 0
groops = []
def isInBound(y, x):
    if y < 0 or y >= len(data) or x < 0 or x >= len(data):
        return False
    return True

def dsf(y, x, group, seen):
    seen.append((y, x))
    notVisited.remove((y, x))
    neighbours = 0
    groupeSize = 0
    fence = 0
    for Y, X in moves:
        dy = y + Y
        dx = x + X
        if isInBound(dy, dx) and data[dy][dx] == group:
            neighbours += 1
            if (dy, dx) not in seen:
                g, f = dsf(dy, dx, group, seen)
                groupeSize += g
                fence += f
    fence += 4 - neighbours
    groupeSize += 1
    return (groupeSize, fence)
    
notVisited = set()
for y in range(len(data)):
    for x in range(len(data[y])):
        notVisited.add((y, x))

i = 0
d = {}
while notVisited:
    y, x = list(notVisited)[0]
    d[i] = dsf(y, x, data[y][x], [])
    i += 1
ans = 0
for key in d:
    x, y = d[key]
    ans += x*y
print(ans)
        