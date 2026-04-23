class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lookup = {}

        l = 0
        max_len = 0

        for r in range(len(s)):
            char = s[r]

            if char not in lookup or l > lookup[char]:
                lookup[char] = r
                max_len = max(max_len, r - l + 1)
            else:
                l = lookup[char] + 1
                lookup[char] = r

        return max_len