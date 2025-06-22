# TrieNode class
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


# Trie class
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True

    def search(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_end_of_word

    def starts_with(self, prefix):
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True



if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    trie.insert("app")
    trie.insert("banana")

    print(trie.search("apple"))    # True
    print(trie.search("app"))      # True
    print(trie.search("appl"))     # False
    print(trie.search("banana"))   # True
    print(trie.starts_with("app")) # True
    print(trie.starts_with("ban")) # True
    print(trie.starts_with("bat")) # False
