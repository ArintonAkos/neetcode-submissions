import heapq 

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(x: int, y: int) -> float:
            return 

        max_heap = []

        for x, y in points:
            d = -(x**2 + y**2)
            heapq.heappush(max_heap, (d, x, y))

            if len(max_heap) > k:
                heapq.heappop(max_heap)
            
        return [(x, y) for _, x, y in max_heap]
