from bisect import bisect_left, bisect_right

class TimeMap:

    def __init__(self):
        self.val = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.val[key].append((timestamp, value))

    def binarySearch(self, values: List[tuple[int, str]], target: int):
        l, r = 0, len(values) - 1
        res = ""

        while l <= r:
            m = (l + r) // 2

            if values[m][0] == target:
                return values[m][1]
            
            if values[m][0] < target:
                # Cehck the left side only
                l = m + 1
                res = values[m][1]
            else:
                # Check the right side only
                r = m - 1

        return res


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.val:
            return ""

        return self.binarySearch(self.val[key], timestamp)
