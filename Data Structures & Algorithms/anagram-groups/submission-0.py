class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        
        def char_idx(c: str) -> int:
            return ord(c) - ord('a')

        for string in strs:
            freq = [0] * 26
            for c in string:
                freq[char_idx(c)] += 1

            groups[tuple(freq)].append(string)

        return list(groups.values())