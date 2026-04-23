class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # [0, 1, 2, 3, 4, 5]
        # [3, 4, 5, 6, 1, 2]
        # (0 + 5) // 2 = 5 // 2 = 2
        

        # t =    1
        # 
        # l =    0, 3
        # r =    5, 5
        # m =    2
        # 
        # n[l] = 3, 6
        # n[r] = 2, 2
        # n[m] = 5, 1 -> return
        
        
        # [0, 1, 2, 3, 4, 5]
        # [1, 2, 3, 4, 5, 6]
        # n[2] = 3
        # t =    1
        # 
        # l =    0
        # r =    5
        # m =    2
        # 
        # n[l] = 1
        # n[r] = 6
        # n[m] = 3
        # def binary_search(left: int, right: int):
        #     if left > right:
        #         return -1

        #     mid = (left + right) // 2

        #     if nums[mid] == target:
        #         return mid

        #     # It means it is in the left proportion
        #     if nums[mid] >= nums[right]:
        #         # Check whether the target is in this range
        #         if target >= nums[left] and target < nums[mid]:
        #             return binary_search(left, mid - 1)

        #         return binary_search(mid + 1, right)
        #     else:
        #         if target > nums[mid] and target <= nums[right]:
        #             return binary_search(mid + 1, right)

        #         return binary_search(left, mid - 1)

        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            if nums[m] >= nums[r]:
                if target >= nums[l] and target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if target > nums[m] and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return -1
                