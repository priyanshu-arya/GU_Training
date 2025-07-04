import java.util.*;

public class SegmentTreeAP {
    static final int MOD = 1_000_000_007;

    static class SegmentTree {
        long[] tree, lazyA, lazyD;
        boolean[] hasLazy;
        int n;

        SegmentTree(int[] A) {
            n = A.length;
            tree = new long[4 * n];
            lazyA = new long[4 * n];
            lazyD = new long[4 * n];
            hasLazy = new boolean[4 * n];
            build(0, 0, n - 1, A);
        }

        void build(int node, int l, int r, int[] A) {
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
            long a = lazyA[node], d = lazyD[node];
            int len = r - l + 1;
            long total = (len * a % MOD + d * ((long) len * (len - 1) / 2) % MOD) % MOD;
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

        void update(int ql, int qr, long a, long d) {
            update(ql, qr, a, d, 0, 0, n - 1);
        }

        void update(int ql, int qr, long a, long d, int node, int l, int r) {
            push(node, l, r);

            if (r < ql || l > qr) return;

            if (ql <= l && r <= qr) {
                long base = (a + (l - ql) * d % MOD + MOD) % MOD;
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

        long query(int ql, int qr) {
            return query(ql, qr, 0, 0, n - 1);
        }

        long query(int ql, int qr, int node, int l, int r) {
            push(node, l, r);

            if (r < ql || l > qr) return 0;

            if (ql <= l && r <= qr) return tree[node];

            int mid = (l + r) / 2;
            long left = query(ql, qr, 2 * node + 1, l, mid);
            long right = query(ql, qr, 2 * node + 2, mid + 1, r);
            return (left + right) % MOD;
        }
    }

    public static int solveOptimized(int n, int[] A, int[][] queries) {
        SegmentTree st = new SegmentTree(A);
        long total = 0;

        for (int[] q : queries) {
            int type = q[0], l = q[1], r = q[2];
            if (type == 1) {
                long base = st.query(l, l);
                st.update(l, r, base, base);
            } else {
                total = (total + st.query(l, r)) % MOD;
            }
        }

        return (int) total;
    }

    public static void main(String[] args) {
        int n = 7;
        int[] A = {1, 4, 5, 1, 6, 7, 8};
        int[][] queries = {
            {1, 1, 6},
            {1, 1, 5},
            {2, 5, 5},
            {2, 3, 4},
            {2, 3, 3}
        };

        System.out.println(solveOptimized(n, A, queries)); // Output: 60
    }
}
