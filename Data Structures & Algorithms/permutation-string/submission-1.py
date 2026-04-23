class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = [0] * 26
        s2_count = [0] * 26
        n, m = len(s1), len(s2)

        if len(s1) > len(s2):
            return False

        def char_idx(c: str) -> int:
            return ord(c) - ord('a')

        for i in range(n):
            s1_count[char_idx(s1[i])] += 1
            s2_count[char_idx(s2[i])] += 1

        # O(26)
        if s1_count == s2_count:
            return True

        for i in range(n, m):
            s2_count[char_idx(s2[i])] += 1
            s2_count[char_idx(s2[i - n])] -= 1

            if s1_count == s2_count:
                return True

        return s1_count == s2_count



