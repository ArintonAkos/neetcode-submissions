class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2

        if len(A) > len(B):
            A, B = B, A

        # 3 + 5 = 8
        # 8 // 2
        # [4, 6, 7, 8, 9] -> 5 len
        # [1, 5, 10] -> 3 len
        # [0, 1, 2, 3, 4, 5, 6, 7]
        # [1, 4, 5, 6, 7, 8, 9, 10]
        # i = 1
        # half = 4

        l, r = 0, len(A) - 1

        while True:
            i = (l + r) // 2
            # 4 - 1 - 2 = 1 -> 1st positino
            j = half - i - 2

            a_left  = A[i] if i >= 0 else float('-inf')
            a_right = A[i + 1] if (i + 1) < len(A) else float('inf')
            b_left  = B[j] if j >= 0 else float('-inf')
            b_right = B[j + 1] if (j + 1) < len(B) else float('inf')

            if a_left <= b_right and b_left <= a_right:
                if total % 2 == 1:
                    return min(a_right, b_right)

                return ( max(a_left, b_left) + min(a_right, b_right) ) / 2.0
            elif a_left > b_right:
                r = i - 1
            else:
                l = i + 1