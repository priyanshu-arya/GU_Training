#include <iostream>
#include <vector>
using namespace std;

class FenwickTree {
    vector<int> tree;
    int n;

public:
    FenwickTree(int size) {
        n = size;
        tree.resize(n + 1, 0);
    }

    void update(int index, int delta) {
        while (index <= n) {
            tree[index] += delta;
            index += index & -index;
        }
    }

    int prefixSum(int index) {
        int result = 0;
        while (index > 0) {
            result += tree[index];
            index -= index & -index;
        }
        return result;
    }

    int rangeSum(int left, int right) {
        return prefixSum(right) - prefixSum(left - 1);
    }
};

int main() {
    FenwickTree ft(10);
    ft.update(3, 5);
    ft.update(5, 2);
    cout << ft.rangeSum(3, 5) << endl; // Output: 7
    return 0;
}
