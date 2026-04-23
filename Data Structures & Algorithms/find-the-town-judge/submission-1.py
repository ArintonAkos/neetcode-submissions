class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegree = [0] * (n + 1)
        outdegree = [0] * (n + 1)

        for ai, bi in trust:
            outdegree[ai] += 1
            indegree[bi] += 1

        for idx, [i, o] in enumerate(zip(indegree[1:], outdegree[1:])):
            # If outdegree is 0 and indegree is n - 1, it is a town judge
            if i == n - 1 and o == 0:
                return idx + 1
        
        return -1