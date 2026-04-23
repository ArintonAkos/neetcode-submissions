import random 

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def partition(left: int, right: int, pivot_index: int) -> int:
            if left >= right:
                return left

            pivot = nums[pivot_index]
            nums[right], nums[pivot_index] = nums[pivot_index], nums[right]
            store_index = left

            for i in range(left, right):
                if nums[i] < pivot:
                    nums[store_index], nums[i] = nums[i], nums[store_index]
                    store_index += 1

            nums[store_index], nums[right] = nums[right], nums[store_index]
            return store_index

        def quicksort(left: int, right: int):
            if left >= right:
                return

            pivot_index = random.randint(left, right)
            pivot_index = partition(left, right, pivot_index)

            quicksort(left, pivot_index - 1)
            quicksort(pivot_index + 1, right)

        quicksort(0, len(nums) - 1)

        return nums
