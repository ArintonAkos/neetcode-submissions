class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = {i: i for i in range(n)}
        rank = {i: 1 for i in range(n)}

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])

            return parent[x]

        def union(x: int, y: int):
            rootX = find(x)
            rootY = find(y)

            if rootX == rootY:
                # No union was made
                return False

            if rank[rootX] < rank[rootY]:
                parent[rootX] = parent[rootY]
            elif rank[rootX] > rank[rootY]:
                parent[rootY] = parent[rootX]
            else:
                parent[rootX] = parent[rootY]
                rank[rootY] += 1

            return True

        res = n
        for u, v in edges:
            res -= 1 if union(u, v) else 0 

        return res