class Solution:
    def validPalindrome(self, s: str) -> bool:
        def palindrome(left: int, right: int, has_used: bool) -> bool:
            while left < right and s[left] == s[right]:
                left  += 1
                right -= 1
            
            if left < right and not has_used:
                return palindrome(left + 1, right, True) or palindrome(left, right - 1, True)
            
            return left >= right
        
        return palindrome(0, len(s) - 1, False)
