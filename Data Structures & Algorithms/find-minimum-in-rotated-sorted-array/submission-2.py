class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def binary_search(left: int, right: int):
            if left == right:
                return nums[left]
            
            # If nums[left] is smaller than the number on the right
            # it means that we found the increasing sequence, 
            # so we just have to return the left-most item
            if nums[left] < nums[right]:
                return nums[left]

            mid = (left + right) // 2

            in_left_portion  = nums[mid] >= nums[left]
            in_right_portion = nums[mid] <= nums[left]

            if in_left_portion:
                return binary_search(mid + 1, right)
            else:
                return binary_search(left,  mid)



        return binary_search(0, len(nums) - 1)
