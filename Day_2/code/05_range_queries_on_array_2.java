import java.util.*;

public class SegmentTreeSolution {
    static final int MOD = 1_000_000_007;

    static class SegmentTree {
        int[] tree;
        int n;

        SegmentTree(int[] A) {
            this.n = A.length;
            this.tree = new int[4 * n];
            build(A, 0, 0, n - 1);
        }

        void build(int[] A, int node, int start, int end) {
            if (start == end) {
                tree[node] = A[start];
            } else {
                int mid = (start + end) / 2;
                build(A, 2 * node + 1, start, mid);
                build(A, 2 * node + 2, mid + 1, end);
                tree[node] = tree[2 * node + 1] + tree[2 * node + 2];
            }
        }

        void update(int index, int value, int node, int start, int end) {
            if (start == end) {
                tree[node] = value;
            } else {
                int mid = (start + end) / 2;
                if (index <= mid) {
                    update(index, value, 2 * node + 1, start, mid);
                } else {
                    update(index, value, 2 * node + 2, mid + 1, end);
                }
                tree[node] = tree[2 * node + 1] + tree[2 * node + 2];
            }
        }

        int query(int L, int R, int node, int start, int end) {
            if (R < start || end < L) return 0;
            if (L <= start && end <= R) return tree[node];
            int mid = (start + end) / 2;
            int left = query(L, R, 2 * node + 1, start, mid);
            int right = query(L, R, 2 * node + 2, mid + 1, end);
            return left + right;
        }
    }

    public static int processQueries(int n, int[] A, int[][] queries) {
        SegmentTree st = new SegmentTree(A);
        long totalSum = 0;

        for (int[] query : queries) {
            int type = query[0];
            int l = query[1];
            int r = query[2];

            if (type == 1) {
                int base = A[l];
                for (int i = l; i <= r; i++) {
                    A[i] = (i - l + 1) * base;
                    st.update(i, A[i], 0, 0, n - 1);
                }
            } else if (type == 2) {
                totalSum = (totalSum + st.query(l, r, 0, 0, n - 1)) % MOD;
            }
        }
        return (int) totalSum;
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

        System.out.println(processQueries(n, A, queries)); // Output: 60
    }
}
