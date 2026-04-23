class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)

        # If s is longer than t, there is no way to have subsequence
        if m > n:
            return False
        
        j = 0
        for c in s:
            while j < n and t[j] != c:
                j += 1

            if j == n:
                return False

            j += 1

        return True