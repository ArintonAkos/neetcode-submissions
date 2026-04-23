class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort(key=lambda x: (x[0], x[1]))

        

        result = [intervals[0]]
        k = 0

        for interval in intervals[1:]:
            if interval[0] <= result[k][1]:
                result[k][1] = max(result[k][1], interval[1])
            else:
                result.append(interval)
                k += 1
        
        return result