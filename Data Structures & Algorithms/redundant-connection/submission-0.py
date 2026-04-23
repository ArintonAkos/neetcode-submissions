class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = {i: i for i in range(1, n + 1)}
        rank = {i: 1 for i in range(1, n + 1)}

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])

            return parent[x]

        def union(x: int, y: int) -> bool:
            rootX = find(x)
            rootY = find(y)

            if rootX == rootY:
                return False

            if rank[rootX] < rank[rootY]:
                parent[rootX] = parent[rootY]
            elif rank[rootY] < rank[rootX]:
                parent[rootY] = parent[rootX]
            else:
                parent[rootX] = parent[rootY]
                rank[rootY] += 1

            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]