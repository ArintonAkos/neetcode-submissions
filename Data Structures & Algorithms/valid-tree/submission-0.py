class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()

        def dfs(i: int):
            if i in visited:
                return

            visited.add(i)

            for dest in adj[i]:
                dfs(dest)

        dfs(0)
        return len(visited) == n