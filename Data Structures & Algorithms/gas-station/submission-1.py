class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        n = len(gas)
        tank = 0
        i = 0
        possible_start = 0

        while i < n:
            tank += gas[i] - cost[i]

            if tank < 0:
                tank = 0
                possible_start = i + 1
            
            i += 1

        return possible_start if possible_start < n else -1