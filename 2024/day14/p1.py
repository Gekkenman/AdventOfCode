import re

with open("input.txt", "r") as f:
    data = []
    for line in f:
        line = line.strip()
        data.append((map(int, re.findall(r"-?\d+", line))))

width = 101
hight = 103
out = []
#px, py, vx, vy = data[0]

grid = [["." for _ in range(width)] for x in range(hight)]
def gprint():
    print("=================")
    for line in grid:
        print("".join(line))


#for i in range(6):
    #newx = (vx * i+ px) % width
    #newy = (vy * i+ py) % hight
    #grid[newy][newx] = "x"
    #gprint()
    #print(newx, newy)
    #grid[newy][newx] = "."

for px, py, vx, vy in data:
    px = (vx * 100+ px) % width
    py = (vy * 100+ py) % hight
    grid[py][px] = "x"
    out.append((px, py))

quadrant = [0, 0, 0, 0]
for x, y in out:
    if x < width // 2 and y < hight // 2: # top left
        quadrant[0] += 1
    elif x > width // 2 and y < hight // 2: # top right
        quadrant[1] += 1
    elif x < width // 2 and y > hight // 2: # bottom left
        quadrant[2] += 1
    elif x > width // 2 and y > hight // 2: # bottem right
        quadrant[3] += 1

ans = 1
for num in quadrant:
    ans *= num
print(ans)