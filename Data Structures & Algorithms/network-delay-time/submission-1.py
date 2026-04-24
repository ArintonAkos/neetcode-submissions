import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for u, v, w in times:
            adj[u].append((v, w))

        distances = {i: float('inf') for i in range(1, n + 1)}
        pq = [(0, k)]
        distances[k] = 0

        while pq:
            d, u = heapq.heappop(pq)

            if d > distances[u]:
                continue

            for v, w in adj[u]:
                d_x = d + w

                if d_x < distances[v]:
                    distances[v] = d_x
                    heapq.heappush(pq, (distances[v], v))
        
        res = max(distances.values())
        return res if res < float('inf') else -1