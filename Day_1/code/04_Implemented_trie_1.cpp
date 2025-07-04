#include <iostream>
#include <unordered_map>
#include <string>
using namespace std;

class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    bool isEndOfWord;

    TrieNode() : isEndOfWord(false) {}
};

class Trie {
private:
    TrieNode* root;

public:
    Trie() {
        root = new TrieNode();
    }

    void insert(const string& word) {
        TrieNode* current = root;
        for (char ch : word) {
            if (!current->children.count(ch)) {
                current->children[ch] = new TrieNode();
            }
            current = current->children[ch];
        }
        current->isEndOfWord = true;
    }

    bool search(const string& word) {
        TrieNode* current = root;
        for (char ch : word) {
            if (!current->children.count(ch)) {
                return false;
            }
            current = current->children[ch];
        }
        return current->isEndOfWord;
    }

    bool startsWith(const string& prefix) {
        TrieNode* current = root;
        for (char ch : prefix) {
            if (!current->children.count(ch)) {
                return false;
            }
            current = current->children[ch];
        }
        return true;
    }
};

int main() {
    Trie trie;
    trie.insert("apple");
    trie.insert("app");
    trie.insert("banana");

    cout << boolalpha;  // print true/false instead of 1/0
    cout << trie.search("apple") << endl;    // true
    cout << trie.search("app") << endl;      // true
    cout << trie.search("appl") << endl;     // false
    cout << trie.search("banana") << endl;   // true
    cout << trie.startsWith("app") << endl;  // true
    cout << trie.startsWith("ban") << endl;  // true
    cout << trie.startsWith("bat") << endl;  // false

    return 0;
}
