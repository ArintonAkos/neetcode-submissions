"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # If we don't have meetings, no days is required
        if not intervals:
            return 0

        intervals.sort(key=lambda x: (x.start, x.end))

        days_last = [intervals[0].end]

        for interval in intervals[1:]:
            # If the meeting starts earlier than any of the meetings would end
            # we need to re-schedule the meeting to another day
            if interval.start >= days_last[0]:
                heapq.heappop(days_last)

            heapq.heappush(days_last, interval.end)
        
        return len(days_last)


