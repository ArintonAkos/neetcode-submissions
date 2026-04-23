class Solution:
    def findMin(self, nums: List[int]) -> int:
        def binary_search(left: int, right: int):
            # If nums[left] is smaller than the number on the right
            # it means that we found the increasing sequence, 
            # so we just have to return the left-most item
            if nums[left] <= nums[right]:
                return nums[left]

            mid = (left + right) // 2

            if nums[mid] >= nums[left]:
                return binary_search(mid + 1, right)
            else:
                return binary_search(left,  mid)

        return binary_search(0, len(nums) - 1)