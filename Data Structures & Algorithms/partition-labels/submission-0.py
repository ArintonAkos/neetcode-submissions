class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        if not s:
            return []

        def char_idx(c: str) -> int:
            return ord(c) - ord('a')

        # 26 characters in english alphabet
        last_index = [-1] * 26

        for i, c in enumerate(s):
            last_index[char_idx(c)] = i

        l, r = 0, last_index[char_idx(s[0])]
        start_idx = 0
        n = len(s)
        res = []

        while l < n:
            r = max(r, last_index[char_idx(s[l])])
            
            if l == r:
                res.append(r - start_idx + 1)
                start_idx = r + 1

            l += 1

        return res