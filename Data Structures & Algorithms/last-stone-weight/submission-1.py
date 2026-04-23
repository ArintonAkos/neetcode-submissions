import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)
        n = len(stones)

        while len(max_heap) > 1:
            heavy1, heavy2 = heapq.heappop(max_heap), heapq.heappop(max_heap)

            if heavy1 == heavy2:
                continue
            
            remaining = abs(heavy1 - heavy2)
            heapq.heappush(max_heap, -remaining)

        return -max_heap[0] if len(max_heap) > 0 else 0

        

