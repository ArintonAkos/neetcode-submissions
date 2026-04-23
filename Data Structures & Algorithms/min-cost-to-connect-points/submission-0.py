class UnionFind:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    # Union x with y
    # If already in the same union, the method returns False
    def union(self, x: int, y: int) -> bool:
        rootX = self.find(x)
        rootY = self.find(y)

        # Already merged
        if rootX == rootY: 
            return False

        if self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        elif self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1

        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        union_find = UnionFind(n)
        #          [     (u,     v,   w)]
        edges: List[tuple[int, int, int]] = []

        def manhattan_d(x1: int, y1: int, x2: int, y2: int):
            return abs(x1 - x2) + abs(y1 - y2)

        for i in range(n):
            for j in range(i + 1, n):
                w = manhattan_d(points[i][0], points[i][1], points[j][0], points[j][1])
                # edges[i].append((j, w))
                # edges[j].append((i, w))
                edges.append((i, j, w))

        # Sort based on the weight
        edges.sort(key=lambda x: x[2])

        res = 0
        for u, v, w in edges:
            if union_find.union(u, v):
                res += w

        return res        




