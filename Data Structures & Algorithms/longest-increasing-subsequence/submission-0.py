from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        
        for num in nums:
            # Ha nagyobb, mint a legnagyobb -> bővítünk
            if not sub or sub[-1] < num:
                sub.append(num)
            else:
                # Megkeressük az első elemet, ami >= num
                idx = bisect_left(sub, num)
                # És lecseréljük, hogy "kisebb számmal" érjük el ugyanazt a hosszt
                sub[idx] = num
                
        return len(sub)