class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k -= 1
        def partition(left: int, right: int, pivot_index: int):
            pivot = nums[pivot_index]
            
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
            store_index = left

            for i in range(left, right):
                if nums[i] > pivot:
                    nums[i], nums[store_index] = nums[store_index], nums[i]
                    store_index += 1    

            nums[right], nums[store_index] = nums[store_index], nums[right]

            return store_index

        def quickSelect(left: int, right: int):
            if left >= right:
                return

            import random
            pivot_index = random.randint(left, right)
            pivot_index = partition(left, right, pivot_index)

            if pivot_index == k:
                return
            elif pivot_index > k:
                quickSelect(left, pivot_index - 1)
            else:
                quickSelect(pivot_index + 1, right)

        quickSelect(0, len(nums) - 1)
        return nums[k]