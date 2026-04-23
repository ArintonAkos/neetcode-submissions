class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        n = len(heights)

        for i, h in enumerate(heights):
            start_idx = i
            while stack and stack[-1][0] > h:
                height, idx = stack.pop()
                width = i - idx
                max_area = max(max_area, height * width)
                start_idx = idx
                
            stack.append((h, start_idx))

        while stack:
            height, idx = stack.pop()
            width = n - idx
            max_area = max(max_area, height * width)

        return max_area