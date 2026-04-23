class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        seen = set()
        x, y, z = target

        for a, b, c in triplets:
            if a > x or b > y or c > z:
                continue

            if a == x and 0 not in seen:
                seen.add(0)

            if b == y and 1 not in seen:
                seen.add(1)
            
            if c == z and 2 not in seen:
                seen.add(2)

            if len(seen) == 3:
                return True

        return False