class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        m, n = len(t), len(s)
        
        i = 0
        j = 0
        while i < m and j < n:
            if s[j] == t[i]:
                j += 1
                i += 1
            else:
                j += 1

        return len(t) - i