class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0

        for i in range(n):
            l, r = i, i
            # While palindrome, expand and increase res
            while l >= 0 and r < n and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            
            l, r = i, i + 1 
            while l >= 0 and r < n and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

        return res

        # What about "abba" ? 
        # What is the expected output ?
        # a, b, bb, abba, a ?