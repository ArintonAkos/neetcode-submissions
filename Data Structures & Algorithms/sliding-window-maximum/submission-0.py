from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()

        for r in range(len(nums)):
            # If it is smaller and older, we can pop it
            while q and q[-1][0] < nums[r]:
                q.pop()

            q.append((nums[r], r))

            # Pop outdated item
            # If the queue-s first item's id is less than the r - k
            if q[0][1] < r - k + 1:
                q.popleft()

            # Let it fill up
            # Do not pop until the first k steps
            if r >= k - 1:
                res.append(q[0][0])

        return res