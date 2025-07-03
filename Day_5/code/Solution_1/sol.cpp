#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

class FenwickTree {
    vector<int> bit;
    int n;

public:
    FenwickTree(int size) {
        n = size;
        bit.assign(n + 2, 0);
    }

    void update(int idx, int delta) {
        while (idx <= n) {
            bit[idx] += delta;
            idx += idx & -idx;
        }
    }

    int query(int idx) {
        int res = 0;
        while (idx > 0) {
            res += bit[idx];
            idx -= idx & -idx;
        }
        return res;
    }
};

int countSpecialPairs(const vector<int>& a) {
    int n = a.size();
    vector<int> prefix(n), suffix(n);
    unordered_map<int, int> freq;

    // Prefix frequencies
    for (int i = 0; i < n; ++i) {
        prefix[i] = ++freq[a[i]];
    }

    // Suffix frequencies
    freq.clear();
    for (int i = n - 1; i >= 0; --i) {
        suffix[i] = ++freq[a[i]];
    }

    FenwickTree bit(n);
    for (int val : suffix)
        bit.update(val, 1);

    int ans = 0;
    for (int i = 0; i < n; ++i) {
        bit.update(suffix[i], -1);
        ans += bit.query(prefix[i] - 1);
    }

    return ans;
}

int main() {
    vector<int> a = {1, 2, 1, 1, 2, 2, 1};
    cout << countSpecialPairs(a) << endl;  // Output: 8
    return 0;
}
