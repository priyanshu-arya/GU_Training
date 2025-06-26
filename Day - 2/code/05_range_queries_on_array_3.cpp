#include <iostream>
#include <vector>
using namespace std;

const int MOD = 1e9 + 7;

struct SegmentTree {
    int n;
    vector<long long> tree, lazyA, lazyD;
    vector<bool> hasLazy;

    SegmentTree(const vector<int>& A) {
        n = A.size();
        tree.assign(4 * n, 0);
        lazyA.assign(4 * n, 0);
        lazyD.assign(4 * n, 0);
        hasLazy.assign(4 * n, false);
        build(0, 0, n - 1, A);
    }

    void build(int node, int l, int r, const vector<int>& A) {
        if (l == r) {
            tree[node] = A[l];
        } else {
            int mid = (l + r) / 2;
            build(2 * node + 1, l, mid, A);
            build(2 * node + 2, mid + 1, r, A);
            tree[node] = (tree[2 * node + 1] + tree[2 * node + 2]) % MOD;
        }
    }

    void push(int node, int l, int r) {
        if (!hasLazy[node]) return;
        long long a = lazyA[node], d = lazyD[node];
        int len = r - l + 1;
        long long total = (len * a % MOD + d * (1LL * len * (len - 1) / 2) % MOD) % MOD;
        tree[node] = total;

        if (l != r) {
            int mid = (l + r) / 2;
            int lenLeft = mid - l + 1;

            lazyA[2 * node + 1] = a;
            lazyD[2 * node + 1] = d;
            hasLazy[2 * node + 1] = true;

            lazyA[2 * node + 2] = (a + lenLeft * d % MOD) % MOD;
            lazyD[2 * node + 2] = d;
            hasLazy[2 * node + 2] = true;
        }

        lazyA[node] = lazyD[node] = 0;
        hasLazy[node] = false;
    }

    void update(int ql, int qr, long long a, long long d, int node = 0, int l = 0, int r = -1) {
        if (r == -1) r = n - 1;
        push(node, l, r);

        if (r < ql || l > qr) return;

        if (ql <= l && r <= qr) {
            long long base = (a + (l - ql) * d % MOD + MOD) % MOD;
            lazyA[node] = base;
            lazyD[node] = d;
            hasLazy[node] = true;
            push(node, l, r);
            return;
        }

        int mid = (l + r) / 2;
        update(ql, qr, a, d, 2 * node + 1, l, mid);
        update(ql, qr, a, d, 2 * node + 2, mid + 1, r);
        tree[node] = (tree[2 * node + 1] + tree[2 * node + 2]) % MOD;
    }

    long long query(int ql, int qr, int node = 0, int l = 0, int r = -1) {
        if (r == -1) r = n - 1;
        push(node, l, r);

        if (r < ql || l > qr) return 0;

        if (ql <= l && r <= qr) return tree[node];

        int mid = (l + r) / 2;
        long long left = query(ql, qr, 2 * node + 1, l, mid);
        long long right = query(ql, qr, 2 * node + 2, mid + 1, r);
        return (left + right) % MOD;
    }
};

int solveOptimized(int n, vector<int>& A, vector<vector<int>>& queries) {
    SegmentTree st(A);
    long long total = 0;

    for (auto& q : queries) {
        int type = q[0], l = q[1], r = q[2];
        if (type == 1) {
            long long base = st.query(l, l);
            st.update(l, r, base, base);
        } else {
            total = (total + st.query(l, r)) % MOD;
        }
    }

    return (int)total;
}

int main() {
    int n = 7;
    vector<int> A = {1, 4, 5, 1, 6, 7, 8};
    vector<vector<int>> queries = {
        {1, 1, 6},
        {1, 1, 5},
        {2, 5, 5},
        {2, 3, 4},
        {2, 3, 3}
    };

    cout << solveOptimized(n, A, queries) << endl;  // Output: 60
    return 0;
}
