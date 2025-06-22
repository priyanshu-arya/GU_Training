import java.util.HashMap;

class TrieNode {
    HashMap<Character, TrieNode> children;
    int wordCount;
    int prefixCount;

    TrieNode() {
        children = new HashMap<>();
        wordCount = 0;
        prefixCount = 0;
    }
}

public class Trie {
    private TrieNode root;

    public Trie() {
        root = new TrieNode();
    }

    public void insert(String word) {
        TrieNode node = root;
        for (char ch : word.toCharArray()) {
            node.children.putIfAbsent(ch, new TrieNode());
            node = node.children.get(ch);
            node.prefixCount++;
        }
        node.wordCount++;
    }

    public int countWordsEqualTo(String word) {
        TrieNode node = root;
        for (char ch : word.toCharArray()) {
            if (!node.children.containsKey(ch)) return 0;
            node = node.children.get(ch);
        }
        return node.wordCount;
    }

    public int countWordsStartingWith(String prefix) {
        TrieNode node = root;
        for (char ch : prefix.toCharArray()) {
            if (!node.children.containsKey(ch)) return 0;
            node = node.children.get(ch);
        }
        return node.prefixCount;
    }

    public void erase(String word) {
        TrieNode node = root;
        for (char ch : word.toCharArray()) {
            TrieNode nextNode = node.children.get(ch);
            nextNode.prefixCount--;
            node = nextNode;
        }
        node.wordCount--;
    }
}


// Java
Trie trie = new Trie();
trie.insert("apple");
trie.insert("apple");
System.out.println(trie.countWordsEqualTo("apple")); // 2
trie.erase("apple");
System.out.println(trie.countWordsEqualTo("apple")); // 1
System.out.println(trie.countWordsStartingWith("app")); // 1
