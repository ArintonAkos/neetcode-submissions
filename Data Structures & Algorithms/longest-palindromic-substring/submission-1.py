class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        
        # Store result index and length
        self.max_len = 0
        self.max_pos = -1

        def findPalindrome(m: int):
            l, r = m, m
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > self.max_len:
                    self.max_len = r - l + 1
                    self.max_pos = l

                l -= 1
                r += 1
            
            l, r = m, m + 1
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > self.max_len:
                    self.max_len = r - l + 1
                    self.max_pos = l

                l -= 1
                r += 1

        for i in range(n):
            findPalindrome(i)

        return s[self.max_pos:self.max_pos+self.max_len]