import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # Min heap because we want to pop in constant time the
        # min elements from the list
        self.min_heap, self.k = nums, k
        heapq.heapify(self.min_heap)
        while len(nums) > k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

        return self.min_heap[0]
