class UnionFind:
    def __init__(self, n: int):
        self.count = n
        self.ranks = [1 for _ in range(n)]
        self.parent = [i for i in range(n)]

    def find(self, x: int):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            rank_x = self.ranks[root_x]
            rank_y = self.ranks[root_y]

            if rank_x > rank_y:
                self.parent[root_y] = root_x
            elif rank_y > rank_x:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.ranks[root_x] += 1
            
            self.count -= 1
            return True
        else:
            # Already 1 union
            return False

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if not isConnected or not isConnected[0]:
            return 0

        n = len(isConnected)
        uf = UnionFind(n)

        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    uf.union(i, j)

        return uf.count