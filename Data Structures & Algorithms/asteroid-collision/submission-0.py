class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # 
        # Array = [2,4,-4,-1]
        # Pos   = [0,1, 2, 3]
        # Size  = [2,4, 4, 1]
        # Dir   = [R,R, L, L]
        if not asteroids:
            return []

        stack = []

        for asteroid in asteroids:

            while stack and asteroid < 0 and stack[-1] > 0:
                diff = asteroid + stack[-1]

                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    asteroid = 0
                    break
                else:
                    stack.pop()
                    asteroid = 0
                    break

            if asteroid:
                stack.append(asteroid)

        return list(stack)