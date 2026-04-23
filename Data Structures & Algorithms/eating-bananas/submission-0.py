from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left  = 1
        right = max(piles)
 
        def calculate_hours_needed(k: int) -> int:
            res = 0

            for pile in piles:
                res += ceil(pile / k)
            
            return res
        
        res = 1
        while left <= right:
            mid = (left + right) // 2

            hours_needed = calculate_hours_needed(mid)

            if hours_needed <= h:
                res = mid
                right = mid - 1
            else:
                left = mid + 1

        return res
