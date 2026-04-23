import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 0 weight, to "k"-th node
        q = [(0, k)]
        adj = defaultdict(list)
        
        for u, v, w in times:
            adj[u].append((v, w))

        distances = {}

        while q:
            w, u = heapq.heappop(q)

            # If we already visited the "U" vertex
            # we can skip it
            if u in distances:
                continue

            # Otherwise the shortest path is "W" 
            distances[u] = w

            for v, w_v in adj[u]:
                # If neighbour have not been visited
                # update the weight to include the road until this point
                # and the weight to the neighbour
                if v not in distances:
                    heapq.heappush(q, (w + w_v, v))

        # If all points haven't been visited, return -1
        if len(distances) != n:
            return -1

        return max(distances.values())