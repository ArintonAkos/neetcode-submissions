class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lookup = {}
        n = len(s)

        l, r = 0, 0
        max_len = 0

        while r < n:
            if s[r] not in lookup or l > lookup[s[r]]:
                lookup[s[r]] = r
                r += 1
                max_len = max(max_len, r - l)
            else:
                l = lookup[s[r]] + 1
                lookup[s[r]] = r
                r += 1

        return max_len