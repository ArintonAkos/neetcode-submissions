class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1

        n = len(nums)
        buckets = [[] for _ in range(n + 1)]

        for num, frequency in freq.items():
            buckets[frequency].append(num)
        # print(f"Buckets: {buckets}")
        res = []
        for i in range(n, 0, -1):
            for num in buckets[i]:
                k -= 1
                res.append(num)
                if k == 0:
                    return res

        