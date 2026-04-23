class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = [0] * 256

        n = len(s)
        l, r = 0, 0
        
        curr_len = 0
        max_len = 0

        def char_idx(c: str) -> int:
            return ord(c)

        while l < n and r < n:
            if freq[char_idx(s[r])] == 0:
                freq[char_idx(s[r])] += 1
                curr_len += 1
                max_len = max(max_len, curr_len)
                r += 1
            else:
                freq[char_idx(s[l])] = 0
                curr_len -= 1
                l += 1

        return max_len
