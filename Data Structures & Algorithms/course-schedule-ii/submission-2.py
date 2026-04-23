class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        deps = defaultdict(list)
        indegree = defaultdict(int)

        # b source a sink
        # b -> a

        for a, b in prerequisites:
            deps[b].append(a)
            indegree[a] += 1

        q = deque()

        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)

        res = []

        while q:
            item = q.popleft()
            res.append(item)

            for dep in deps[item]:
                indegree[dep] -= 1
                if indegree[dep] == 0:
                    q.append(dep)
        
        # print(f"Res: {res} | Prerequisites: {prerequisites} | deps: {deps} | Indegree: {indegree}")

        return res if len(res) == numCourses else []