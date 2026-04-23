class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        res = [intervals[0]]
        k = 1
        i = 1
        n = len(intervals)

        while i < n:
            # If can be merged, no new insertion needed, just merge them
            if res[k - 1][1] >= intervals[i][0]:
                res[k - 1][1] = max(intervals[i][1], res[k - 1][1])
            else:
                res.append(intervals[i])
                k += 1

            i += 1

        return res


