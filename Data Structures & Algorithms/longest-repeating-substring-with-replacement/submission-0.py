class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        
        l = 0
        res = 0
        count = defaultdict(int)
        max_f = 0

        for r in range(n):
            count[s[r]] += 1
            max_f = max(max_f, count[s[r]])

            while r - l + 1 - max_f > k:
                count[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)

        return res    
        