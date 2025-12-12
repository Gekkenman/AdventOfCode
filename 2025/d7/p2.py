class Node:
    left = None
    right = None

    def __init__(self, score, pos):
        self.score = score
        self.pos = pos

    def __str__(self):
        return f"pos: {self.pos}, score: {self.score}, left: {"True" if self.left else "False"}, right: {"True" if self.right else "False"}"


def main():
    nodeList = {}
    with open("input.txt", "r") as f:
        grid = list(map(list, f.read().strip().split("\n")))

        for y, row in enumerate(grid):
            for x, char in enumerate(row):
                if char == "S":
                    head = Node(1, (y, x))
                    nodeList[(y, x)] = head
                    break
                else:
                    continue
                break

    # can be done bether with min-heap than you don't need the sort in the end
    q = [head]

    while q:
        node = q.pop(0)
        y, x = node.pos
        dy = y + 1
        while dy < len(grid):
            if grid[dy][x - 1] == "^":
                if (dy, x - 1) in nodeList:
                    nodeList[dy, x - 1].score += node.score
                    node.left = nodeList[dy, x - 1]
                else:
                    newNode = Node(node.score, (dy, x - 1))
                    nodeList[(dy, x - 1)] = newNode
                    node.left = newNode
                    q.append(newNode)
                break
            dy += 1

        dy = y + 1
        while dy < len(grid):
            if grid[dy][x + 1] == "^":
                if (dy, x + 1) in nodeList:
                    nodeList[dy, x + 1].score += node.score
                    node.right = nodeList[dy, x + 1]
                else:
                    newNode = Node(node.score, (dy, x + 1))
                    nodeList[(dy, x + 1)] = newNode
                    node.right = newNode
                    q.append(newNode)
                break
            dy += 1
        q.sort(key=lambda node: node.pos)

    score = 0
    for key in nodeList:
        y, x = key
        node = nodeList[key]
        grid[y][x] = node.score
        if not node.left:
            score += node.score
        if not node.right:
            score += node.score

    #for row in grid:
    #    print("".join(list(map(str, row))))

    print(score)




if __name__ == "__main__":
    main()
