import heapq 

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(x: int, y: int) -> float:
            return x**2 + y**2

        max_heap = []

        for x, y in points:
            d = distance(x, y)

            if len(max_heap) >= k:
                heap_max_d = -max_heap[0][0]
                if heap_max_d < d:
                    continue
                # Get out the largest element
                heapq.heappop(max_heap)

            heapq.heappush(max_heap, (-d, x, y))
            
        return [(x, y) for _, x, y in max_heap]
