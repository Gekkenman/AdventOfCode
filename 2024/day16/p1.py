class Grid:
    def __init__(self, fileName):
        self.grid = self.generate2DGrid(fileName)
        self.start = (len(self.grid) - 2, 1)
        self.end = (1, len(self.grid[0]) - 2)

    def generate2DGrid(self, fileName):
        with open(fileName, "r") as f:
            grid = list(map(list, f.read().strip().split("\n")))
        return grid


class Node:
    parents = set()

    def __init__(self, pos, score, dir):
        self.pos = pos
        self.score = score
        self.dir = dir

    def __repr__(self):
        return f"({self.pos[0]}, {self.pos[1]}), Direction: ({self.dir[0]}, {self.dir[1]})"

    def __str__(self):
        return f"({self.pos[0]}, {self.pos[1]}), Direction: ({self.dir[0]}, {self.dir[1]})"

class WeightedGraph:
    def __init__(self, grid):
        self.head = self.generateGraph(grid)
        self.edegs = {}

    def generateGraph(self, grid):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # add head node
        head = Node(grid.start, 0, weighted graph(0, 1))
        curNode = head
        seen = []

        for newDir in directions:
            # going same direction
            nY = curNode.pos[0] + newDir[0]
            nX = curNode.pos[1] + newDir[1]
            if grid.grid[nY][nX] == "#":
                continue

            if newDir == curNode.dir:
                self.edges[curNode] = (Node((nY, nX), curNode + 1), newDir)
            else:
                curNode.neighbours.append()

            curNode.neighbours.sort(key=lambda x: x.score)
        seen.append(curNode)
        print(curNode.neighbours)





def main():
    grid = Grid("example1.txt")
    wg = WeightedGraph(grid)
    return 0




if __name__ == "__main__":
    main()
