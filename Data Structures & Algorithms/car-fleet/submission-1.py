class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = []
        n = len(position)

        for i in range(n):
            pair.append((position[i], speed[i]))
        
        pair.sort(key=lambda x: x[0], reverse=True)

        stack = []
        for pos, speed in pair:
            arrive_time = (target - pos) / speed

            if not stack or arrive_time > stack[-1]:
                stack.append(arrive_time)
        
        return len(stack)