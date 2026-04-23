from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegrees = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for src, dst in prerequisites:
            indegrees[dst] += 1
            adj[src].append(dst)

        q = deque()
        for i, indegree in enumerate(indegrees):
            if indegree == 0:
                q.append(i)

        res = deque()
        v_count = 0

        while q:
            curr = q.popleft()
            
            res.appendleft(curr)
            v_count += 1

            for dst in adj[curr]:
                indegrees[dst] -= 1

                if indegrees[dst] == 0:
                    q.append(dst)

        return list(res) if v_count == numCourses else []