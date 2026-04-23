class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def char_id(c: str) -> int:
            if c >= "a":
                # Add a 26 offset
                return ord(c) - ord("a") + 26

            return ord(c) - ord("A")

        target_counts = [0] * 52

        for c in t:
            target_counts[char_id(c)] += 1

        window_counts = [0] * 52

        need = 0
        for count in target_counts:
            if count > 0:
                need += 1

        have = 0
        res, res_len = [-1, -1], float('inf')
        l = 0

        for r in range(len(s)):
            c = s[r]
            idx = char_id(c)

            window_counts[idx] += 1

            if target_counts[idx] > 0 and window_counts[idx] == target_counts[idx]:
                have += 1

            while have == need:
                if (r - l + 1) < res_len:
                    res_len = r - l + 1
                    res = [l, r]

                idx = char_id(s[l])
                window_counts[idx] -= 1

                if target_counts[idx] > 0 and window_counts[idx] < target_counts[idx]:
                    have -= 1

                l += 1

        l, r = res
        return s[l:r+1] if res_len != float('inf') else ""