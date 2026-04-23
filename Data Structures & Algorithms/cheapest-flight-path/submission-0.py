class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)

        for flight in flights:
            u, v, w = flight
            adj[u].append((v, w))

        #       (w, step, vertex)
        heap = [(0, 0,    src)]
        visited_in_stops = [float('inf')] * n
        distances = []
        while heap:
            cost, stops, u = heapq.heappop(heap)

            if u == dst:
                return cost

            # Equal should not stop it since, we can have K stops
            # Maybe we use all K stops and the next destination is the dst
            # that we search for
            if stops > k:
                continue

            # If we already been there in less than or equal stops
            # it means there's no need to go futher
            if visited_in_stops[u] <= stops:
                continue

            visited_in_stops[u] = stops

            for v, w in adj[u]:
                heapq.heappush(heap, (cost + w, stops + 1, v))
        
        return -1
