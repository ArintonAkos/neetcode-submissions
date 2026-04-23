"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True

        intervals.sort(key=lambda x: (x.start, x.end))
        prev_end = intervals[0].end

        for interval in intervals[1:]:
            if interval.start < prev_end:
                return False
            else:
                prev_end = interval.end

        return True