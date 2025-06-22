#include <unordered_map>
#include <string>

class TrieNode {
public:
    std::unordered_map<char, TrieNode*> children;
    int wordCount = 0;
    int prefixCount = 0;
};

class Trie {
private:
    TrieNode* root;

public:
    Trie() {
        root = new TrieNode();
    }

    void insert(std::string word) {
        TrieNode* node = root;
        for (char ch : word) {
            if (!node->children.count(ch)) {
                node->children[ch] = new TrieNode();
            }
            node = node->children[ch];
            node->prefixCount++;
        }
        node->wordCount++;
    }

    int countWordsEqualTo(std::string word) {
        TrieNode* node = root;
        for (char ch : word) {
            if (!node->children.count(ch)) return 0;
            node = node->children[ch];
        }
        return node->wordCount;
    }

    int countWordsStartingWith(std::string prefix) {
        TrieNode* node = root;
        for (char ch : prefix) {
            if (!node->children.count(ch)) return 0;
            node = node->children[ch];
        }
        return node->prefixCount;
    }

    void erase(std::string word) {
        TrieNode* node = root;
        for (char ch : word) {
            TrieNode* nextNode = node->children[ch];
            nextNode->prefixCount--;
            node = nextNode;
        }
        node->wordCount--;
    }
};

// C++
Trie trie;
trie.insert("apple");
trie.insert("apple");
std::cout << trie.countWordsEqualTo("apple") << std::endl; // 2
trie.erase("apple");
std::cout << trie.countWordsEqualTo("apple") << std::endl; // 1
std::cout << trie.countWordsStartingWith("app") << std::endl; // 1
