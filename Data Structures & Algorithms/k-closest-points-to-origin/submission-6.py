import heapq 

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(idx: int) -> float:
            return points[idx][0] ** 2 + points[idx][1] ** 2

        def partition(left: int, right: int, pivot_index: int):
            pivot_dist = dist(pivot_index)

            points[pivot_index], points[right] = points[right], points[pivot_index]

            store_index = left

            for i in range(left, right):
                if dist(i) < pivot_dist:
                    points[store_index], points[i] = points[i], points[store_index]
                    store_index += 1

            points[right], points[store_index] = points[store_index], points[right]
            return store_index
        
        def quick_select(left: int, right: int, k: int):
            if left >= right:
                return 
            
            import random
            pivot_index = random.randint(left, right)

            pivot_final_index = partition(left, right, pivot_index)

            if pivot_final_index == k:
                return
            elif pivot_final_index < k:
                quick_select(pivot_final_index + 1, right, k)
            else:
                quick_select(left, pivot_final_index -1, k)

        quick_select(0, len(points) - 1, k)
        return points[:k]