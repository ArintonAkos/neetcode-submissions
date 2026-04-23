from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegrees = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for nxt, pre in prerequisites:
            indegrees[nxt] += 1
            adj[pre].append(nxt)

        q = deque()
        for i, indegree in enumerate(indegrees):
            if indegree == 0:
                q.append(i)

        res = []

        while q:
            curr = q.popleft()
            
            res.append(curr)

            for dst in adj[curr]:
                indegrees[dst] -= 1

                if indegrees[dst] == 0:
                    q.append(dst)

        return res if len(res) == numCourses else []