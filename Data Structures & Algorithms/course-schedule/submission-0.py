from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for src, dst in prerequisites:
            indegree[dst] += 1
            adj[src].append(dst)

        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        processed_vertices = 0
        while q:
            curr = q.popleft()
            processed_vertices += 1

            for dst in adj[curr]:
                indegree[dst] -= 1
                if indegree[dst] == 0:
                    q.append(dst)

        return processed_vertices == numCourses