class TrieNode:
    def __init__(self):
        self.children = {}
        self.wordCount = 0
        self.prefixCount = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node.prefixCount += 1
        node.wordCount += 1

    def countWordsEqualTo(self, word: str) -> int:
        node = self.root
        for ch in word:
            if ch not in node.children:
                return 0
            node = node.children[ch]
        return node.wordCount

    def countWordsStartingWith(self, prefix: str) -> int:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return 0
            node = node.children[ch]
        return node.prefixCount

    def erase(self, word: str) -> None:
        node = self.root
        stack = []
        for ch in word:
            stack.append((node, ch))
            node = node.children[ch]
            node.prefixCount -= 1
        node.wordCount -= 1


trie = Trie()
trie.insert("apple")
trie.insert("apple")
print(trie.countWordsEqualTo("apple"))     # 2
print(trie.countWordsStartingWith("app"))  # 2
trie.erase("apple")
print(trie.countWordsEqualTo("apple"))     # 1
print(trie.countWordsStartingWith("app"))  # 1
