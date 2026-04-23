class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        last = arr[n - 1]
        
        # Input: arr = [2,4,5,3,1,2]
        # tmp = 1
        # arr[n - 2] = arr[n - 1] -> 2
        # arr[n - 2] = 2
        # arr[n - 1] = max(2, 2)
        # tmp = 3
        # arr[n - 3] = arr[n - 2] -> 

        for i in range(n - 2, -1, -1):
            tmp = arr[i]
            # arr[n - 1] always stores the largest number so far
            arr[i] = arr[n - 1]
            # the new largest number is either the current number or the max so far
            arr[n - 1] = max(tmp, arr[i])

        arr[n - 1] = -1

        return arr