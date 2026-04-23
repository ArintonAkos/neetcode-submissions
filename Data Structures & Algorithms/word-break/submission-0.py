class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        max_len = max(len(w) for w in word_set)
        # Start from the "0"-th index
        n = len(s)
        q = deque([0])
        visited = {0}

        while q:
            i = q.popleft()

            if i == n:
                return True

            for j in range(i + 1, min(i + max_len, n) + 1):
                chunk = s[i:j]

                if chunk in word_set:
                    if j not in visited:
                        visited.add(j)
                        q.append(j)

        return False