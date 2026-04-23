class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(left: int, right: int, target: int) -> int:
            if left > right:
                return -1
            
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return binary_search(mid + 1, right, target)
            else:
                return binary_search(left, mid - 1, target)

        return binary_search(0, len(nums) - 1, target)
