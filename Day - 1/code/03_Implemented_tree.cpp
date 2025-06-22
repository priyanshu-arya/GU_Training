#include <iostream>
#include <vector>
#include <string>
using namespace std;

class TreeNode {
public:
    string data;
    vector<TreeNode*> children;

    TreeNode(string data) : data(data) {}

    void addChild(TreeNode* child) {
        children.push_back(child);
    }
};

class Tree {
private:
    TreeNode* root;

public:
    Tree(TreeNode* root) : root(root) {}

    void printTree(TreeNode* node, int level = 0) {
        if (!node) return;
        cout << string(level * 2, ' ') << node->data << endl;
        for (TreeNode* child : node->children) {
            printTree(child, level + 1);
        }
    }

    void printTree() {
        printTree(root);
    }

    TreeNode* find(string data, TreeNode* node) {
        if (!node) return nullptr;
        if (node->data == data) return node;
        for (TreeNode* child : node->children) {
            TreeNode* result = find(data, child);
            if (result) return result;
        }
        return nullptr;
    }

    TreeNode* find(string data) {
        return find(data, root);
    }

    int getHeight(TreeNode* node) {
        if (node->children.empty()) return 1;
        int maxHeight = 0;
        for (TreeNode* child : node->children) {
            maxHeight = max(maxHeight, getHeight(child));
        }
        return 1 + maxHeight;
    }

    int getHeight() {
        return getHeight(root);
    }

    int countNodes(TreeNode* node) {
        int count = 1;
        for (TreeNode* child : node->children) {
            count += countNodes(child);
        }
        return count;
    }

    int countNodes() {
        return countNodes(root);
    }

    void printList(TreeNode* node) {
        cout << node->data << " ";
        for (TreeNode* child : node->children) {
            printList(child);
        }
    }

    void printList() {
        printList(root);
    }
};

int main() {
    TreeNode* root = new TreeNode("Electronics");

    TreeNode* laptop = new TreeNode("Laptop");
    laptop->addChild(new TreeNode("Mac"));
    laptop->addChild(new TreeNode("Dell"));

    TreeNode* phone = new TreeNode("Phone");
    phone->addChild(new TreeNode("iPhone"));
    phone->addChild(new TreeNode("Samsung"));

    TreeNode* tv = new TreeNode("TV");
    tv->addChild(new TreeNode("Sony"));
    tv->addChild(new TreeNode("LG"));

    root->addChild(laptop);
    root->addChild(phone);
    root->addChild(tv);

    Tree tree(root);

    cout << "Tree structure:\n";
    tree.printTree();

    cout << "\nSearch for 'iPhone':\n";
    TreeNode* found = tree.find("iPhone");
    cout << "Found: " << (found ? found->data : "Not found") << endl;

    cout << "\nTree height: " << tree.getHeight() << endl;
    cout << "Total nodes: " << tree.countNodes() << endl;

    cout << "Tree values in sequence: ";
    tree.printList();
    cout << endl;

    return 0;
}
