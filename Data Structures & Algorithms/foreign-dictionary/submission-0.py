from collections import deque

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = defaultdict(set)
        indegree = {char: 0 for word in words for char in word}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1.startswith(w2):
                return ""

            for j in range(min_len):
                if w1[j] == w2[j]:
                    continue

                if w2[j] not in graph[w1[j]]:
                    graph[w1[j]].add(w2[j])
                    indegree[w2[j]] += 1
                
                break
        
        q = deque()

        for c, d in indegree.items():
            if d == 0:
                q.append(c)

        res = []
        while q:
            u = q.popleft()
            res.append(u)

            for v in graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)

        if len(res) != len(indegree):
            return ""

        return "".join(res)
        

