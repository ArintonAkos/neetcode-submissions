import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = defaultdict(set)

        for [u, v], p in zip(edges, succProb):
            adj[u].add((v, p))
            adj[v].add((u, p))

        print(f"Adj: {adj}")

        pq = [(-1.0, start_node)]
        max_probs = {start_node: 1.0}

        while pq:
            curr_prob, u = heapq.heappop(pq)
            curr_prob = -curr_prob

            if u == end_node:
                return curr_prob

            if curr_prob < max_probs.get(u, 0):
                continue

            for v, edge_prob in adj[u]:
                new_prob = curr_prob * edge_prob

                if new_prob > max_probs.get(v, 0):
                    heapq.heappush(pq, (-(edge_prob * curr_prob), v))
                    max_probs[v] = new_prob

        return 0.0