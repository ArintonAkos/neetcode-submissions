class TrieNode:
    def __init__(self):
        self.children = {}
        self.isLeaf = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()

            curr = curr.children[c]

        curr.isLeaf = True

    def get(self, c: str) -> None:
        curr = self.root
        return None if c not in curr.children else curr.children[c]

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()

        for word in words:
            trie.add(word)

        m, n = len(board), len(board[0])
        self.res = []
        self.dir_x = [0, 1, 0, -1]
        self.dir_y = [1, 0, -1, 0]

        def backtrack(i: int, j: j, word: str, node: Optional[TrieNode]):
            if not node or board[i][j] == '#':
                return 

            car = board[i][j]
            word = word + car

            # print(f"Word: {word} | Node: {node.isLeaf} | Car: {car}")
            if node.isLeaf:
                self.res.append(word)
                # Reset to prevent adding it to the result again
                node.isLeaf = False
            
            board[i][j] = '#'

            for x, y in zip(self.dir_x, self.dir_y):
                new_i, new_j = i + x, j + y
                if new_i < 0 or new_j < 0 or new_i >= m or new_j >= n:
                    continue

                next_char = board[new_i][new_j]
                backtrack(new_i, new_j, word, node.children.get(next_char))

            board[i][j] = car

        for i in range(m):
            for j in range(n):
                # print(f"Board[{i}][{j}] : {board[i][j]}")
                backtrack(i, j, "", trie.get(board[i][j]))

        return self.res