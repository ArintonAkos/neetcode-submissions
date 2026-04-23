class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            if stack:
                while stack and temperatures[stack[-1]] < temp:
                    idx = stack.pop()
                    # The number of waiting for the idx-th item
                    # is the currently max number - the idx of the 
                    # item that we update
                    res[idx] = i - idx
                
            stack.append(i)
        
        return res

        