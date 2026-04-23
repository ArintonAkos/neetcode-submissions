class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_area = 0

        def area(i: int, j: int):
            height = min(heights[i], heights[j])
            width = j - i

            return width * height

        while l < r:
            max_area = max(max_area, area(l, r))
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_area