class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        m, n = len(t), len(s)
        
        i = 0
        j = 0
        for c in t:
            while j < n and s[j] != c:
                j += 1

            if j == n:
                break

            j += 1
            i += 1

        return len(t) - i