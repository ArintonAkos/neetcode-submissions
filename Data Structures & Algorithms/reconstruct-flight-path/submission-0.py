import heapq

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for u, v in tickets:
            # No set, because tickets can be duplicated
            # graph[v] not updated, because Graph is directed
            heapq.heappush(graph[u], v)

        path = deque()
        
        def dfs(u: int):
            stack = [u]

            while stack:
                curr = stack[-1]
                
                if graph[curr]:
                    v = heapq.heappop(graph[curr])
                    stack.append(v)
                else:
                    final_node = stack.pop()
                    path.appendleft(final_node)

        src = "JFK"
        dfs(src)

        return list(path)


        