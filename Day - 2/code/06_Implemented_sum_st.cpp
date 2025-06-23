#include <iostream>
using namespace std;

class SegmentTree {
private:
    struct Node {
        int start, end, data;
        Node* left;
        Node* right;

        Node(int s, int e) : start(s), end(e), data(0), left(nullptr), right(nullptr) {}
    };

    Node* root;

    Node* construct(int arr[], int start, int end) {
        if (start == end) {
            Node* leaf = new Node(start, end);
            leaf->data = arr[start];
            return leaf;
        }

        Node* node = new Node(start, end);
        int mid = (start + end) / 2;
        node->left = construct(arr, start, mid);
        node->right = construct(arr, mid + 1, end);
        node->data = node->left->data + node->right->data;
        return node;
    }

    void display(Node* node) {
        if (!node) return;

        string left = node->left ? "[" + to_string(node->left->start) + "-" + to_string(node->left->end) + "] => " + to_string(node->left->data) : "No left child";
        string right = node->right ? "[" + to_string(node->right->start) + "-" + to_string(node->right->end) + "] => " + to_string(node->right->data) : "No right child";
        string curr = "[" + to_string(node->start) + "-" + to_string(node->end) + "] => " + to_string(node->data);

        cout << left << " <= " << curr << " => " << right << "\n\n";

        display(node->left);
        display(node->right);
    }

    int query(Node* node, int qsi, int qei) {
        if (node->start >= qsi && node->end <= qei) return node->data;
        if (node->end < qsi || node->start > qei) return 0;

        return query(node->left, qsi, qei) + query(node->right, qsi, qei);
    }

    int update(Node* node, int index, int value) {
        if (index < node->start || index > node->end) return node->data;

        if (node->start == node->end) {
            node->data = value;
            return node->data;
        }

        int left = update(node->left, index, value);
        int right = update(node->right, index, value);
        node->data = left + right;
        return node->data;
    }

public:
    SegmentTree(int arr[], int n) {
        root = construct(arr, 0, n - 1);
    }

    void display() {
        display(root);
    }

    int query(int qsi, int qei) {
        return query(root, qsi, qei);
    }

    void update(int index, int value) {
        root->data = update(root, index, value);
    }

    void updateRange(int start, int end, int value) {
        for (int i = start; i <= end; i++) {
            root->data = update(root, i, value);
        }
    }
};

// Example usage
int main() {
    int arr[] = {1, 3, 5, 7, 9, 11};
    int n = sizeof(arr) / sizeof(arr[0]);
    SegmentTree st(arr, n);

    st.display();

    cout << "Query(1, 3): " << st.query(1, 3) << endl; // 15
    st.update(1, 10);
    cout << "Query(1, 3) after update: " << st.query(1, 3) << endl; // 22

    st.updateRange(3, 5, 20);
    cout << "Query(1, 3) after range update: " << st.query(1, 3) << endl; // 22

    st.display();
    return 0;
}
