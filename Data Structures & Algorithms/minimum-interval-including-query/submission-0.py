import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        if not queries:
            return []

        intervals.sort()

        sorted_queries = sorted(enumerate(queries), key=lambda x: x[1])

        # [[1,3],[2,3],[3,7],[6,6]] -> already sorted
        # let's say [-2, -1], [0, 1] is there
        # we have to skip values that :
        #  - end earlier than current query
        #  - start earlier than current query

        # we need to keep K number of intervals, which could be a possible solution
        # then get the one with the smallest solution. if the query can use it, 
        # we don't pop it just return the length of it. Otherwise we pop it and never use it
        # [2,3,1,7,6,8] -> [1,2,3,6,7,8]

        i = 0
        pq = []
        res = [-1] * len(queries)

        for original_index, query_val in sorted_queries:
            while i < len(intervals) and intervals[i][0] <= query_val:
                start, end = intervals[i]
                length = end - start + 1
                heapq.heappush(pq, (length, end))
                i += 1
            
            # We try to get somethign from the pq, until it fits into our query
            while pq and pq[0][1] < query_val:
                heapq.heappop(pq)

            if pq:
                res[original_index] = pq[0][0]

        return res