class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        # Sort intervals by start date
        intervals.sort(key=lambda x: (x[0], x[1]))

        # Does it matter if we have 
        # [1, 3], [1, 4], [1, 2] or
        # [1, 2], [1, 3], [1, 4] -> This seems to be easier, we just keep the first that doesn't overlap
        # and increment the res when something would overlap
        # Therefore we need a custom comparator that takes the 2nd value in account as well.
        res = 0
        n = len(intervals)
        prev_end = intervals[0][1]

        for start, end in intervals[1:]:
            # If current interval starts earlier than the one before ends 
            if start < prev_end:
                res += 1
                prev_end = min(end, prev_end)
            else:
                prev_end = end
        
        return res
