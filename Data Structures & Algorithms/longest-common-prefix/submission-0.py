class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        for i, c in enumerate(strs[0]):
            for other_str in strs[1:]:
                if i == len(other_str) or other_str[i] != c:
                    return strs[0][:i]

        return strs[0]
        
