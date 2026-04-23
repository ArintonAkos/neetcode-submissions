from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not beginWord:
            return 0        

        nei = defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                nei[pattern].append(word)

        q = deque([beginWord])
        length = 1
        visited = set([beginWord])

        # print(f"Nei is: {nei}")

        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                
                # print(f"Curr is: {curr}")
                if curr == endWord:
                    return length

                for i in range(len(curr)):
                    pattern = curr[:i] + "*" + curr[i+1:]
                    for w in nei[pattern]:
                        # print(f"Checking: {w} for {pattern}")
                        if w not in visited:
                            # print("It is not visited !")
                            visited.add(w)
                            q.append(w)

            length += 1

        return 0