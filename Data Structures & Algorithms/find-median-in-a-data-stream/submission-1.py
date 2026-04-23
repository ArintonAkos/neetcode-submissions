import heapq

class MedianFinder:

    def __init__(self):
        # Max-Heap
        self.small = []
        # Min-Heap
        self.large = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)

        small_max = heapq.heappop(self.small)
        heapq.heappush(self.large, -small_max)

        if len(self.large) > len(self.small):
            large_min = heapq.heappop(self.large)
            heapq.heappush(self.small, -large_min)


    def findMedian(self) -> float:
        n = len(self.small) + len(self.large)

        if n % 2 == 0:
            return (-self.small[0] + self.large[0]) / 2

        return -self.small[0]

        