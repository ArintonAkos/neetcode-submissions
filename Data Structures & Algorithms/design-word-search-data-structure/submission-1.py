class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isLeaf = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        
        for c in word:
            idx = ord(c) - ord('a')
            if curr.children[idx] is None:
                curr.children[idx] = TrieNode()

            curr = curr.children[idx]

        curr.isLeaf = True

    def search(self, word: str) -> bool:
        def dfs(node: TrieNode, j: int) -> bool:
            if j == len(word):
                return node.isLeaf

            if word[j] == '.':
                for child in node.children:
                    if child is None:
                        continue

                    res = dfs(child, j + 1)
                    if res:
                        return True

                return False
            else:
                curr = node.children[ord(word[j]) - ord('a')]
                return curr is not None and dfs(curr, j + 1)

        return dfs(self.root, 0)
