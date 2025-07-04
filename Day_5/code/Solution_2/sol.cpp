#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
using namespace std;

class FenwickTree {
    vector<int> tree;
    int n;

public:
    FenwickTree(int size) {
        n = size;
        tree.assign(n + 1, 0);
    }

    void update(int index, int delta) {
        while (index <= n) {
            tree[index] += delta;
            index += index & -index;
        }
    }

    int query(int index) {
        int result = 0;
        while (index > 0) {
            result += tree[index];
            index -= index & -index;
        }
        return result;
    }
};

int main() {
    vector<int> a = {3, 3, 1, 6, 1};
    int n = a.size();

    // Coordinate compression
    set<int> sortedSet(a.begin(), a.end());
    vector<int> sortedList(sortedSet.begin(), sortedSet.end());

    map<int, int> compressMap;
    for (int i = 0; i < sortedList.size(); ++i) {
        compressMap[sortedList[i]] = i + 1;
    }

    FenwickTree fenwick(sortedList.size());
    for (int i = 1; i <= sortedList.size(); ++i) {
        fenwick.update(i, 1);
    }

    map<int, int> rankMap;
    for (int val : sortedList) {
        int index = compressMap[val];
        rankMap[val] = fenwick.query(index - 1);
    }

    for (int val : a) {
        cout << rankMap[val] << endl;
    }

    return 0;
}
