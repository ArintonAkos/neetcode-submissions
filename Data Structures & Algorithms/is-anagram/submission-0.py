class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq = [0] * 26

        def char_id(c: str) -> int:
            return ord(c) - ord('a')
        
        for c in s:
            freq[char_id(c)] += 1

        for c in t:
            freq[char_id(c)] -= 1

        for c in freq:
            if c != 0:
                return False

        return True