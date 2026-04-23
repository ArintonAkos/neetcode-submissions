class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        def area(i: int, j: int):
            if i > j:
                i, j = j, i

            if i == j:
                return heights[i]
            
            h = min(heights[i], heights[j])
            w = j - i + 1

            return h * w

        stack = []
        max_area = 0
        n = len(heights)

        for i, h in enumerate(heights):
            if stack and h < stack[-1][0]:
                # If current element is lower than stack top:
                # Pop everything until a lower or equal rectangle is at the top
                last_idx = None
                while stack and stack[-1][0] > h:
                    height, idx = stack.pop()
                    width = i - idx

                    area = height * width
                    max_area = max(max_area, area)
                    last_idx = idx

                stack.append((h, last_idx))
            else:
                stack.append((h, i))
        ##################
       #717224 
        ###################
        # #
        # #
        # #
        # #  #
        # #  #
        # ####
        ######
        # print(f"At this point : {max_area} | {stack}")

        while stack:
            height, idx = stack.pop()
            width = n - idx
            # print(f"H: {height} | Idx: {idx} | Width: {width} | Area: {height * width}")
            area = height * width
            max_area = max(max_area, area)

        return max_area