'''
apply_arithmetic(l, r, a, d): set A[i] = a + (i - l) * d

range_query(l, r): sum from A[l] to A[r]

Our goal is to process all queries efficiently, especially for large n and q (up to 1e5).

Optimization Strategy

To handle this efficiently, we need:

A Segment Tree that supports:

    Range assignment of an arithmetic progression.

    Range sum queries.

A segment tree node must store:

    sum: total sum of the segment

    lazy_a, lazy_d: parameters for a pending arithmetic progression (AP) update
    where:

        A[i] = a + (i - l) * d

'''

MOD = 10**9 + 7

class SegmentTree:
    def __init__(self, A):
        self.n = len(A)
        self.tree = [0] * (4 * self.n)
        self.lazy_a = [0] * (4 * self.n)
        self.lazy_d = [0] * (4 * self.n)
        self.has_lazy = [False] * (4 * self.n)
        self.build(0, 0, self.n - 1, A)

    def build(self, node, l, r, A):
        if l == r:
            self.tree[node] = A[l]
        else:
            mid = (l + r) // 2
            self.build(2 * node + 1, l, mid, A)
            self.build(2 * node + 2, mid + 1, r, A)
            self.tree[node] = (self.tree[2 * node + 1] + self.tree[2 * node + 2]) % MOD

    def push(self, node, l, r):
        if self.has_lazy[node]:
            a = self.lazy_a[node]
            d = self.lazy_d[node]
            length = r - l + 1
            total = (length * a + d * (length * (length - 1) // 2)) % MOD
            self.tree[node] = total

            if l != r:
                mid = (l + r) // 2
                len_left = mid - l + 1
                self.lazy_a[2 * node + 1] = a
                self.lazy_d[2 * node + 1] = d
                self.has_lazy[2 * node + 1] = True

                self.lazy_a[2 * node + 2] = (a + len_left * d) % MOD
                self.lazy_d[2 * node + 2] = d
                self.has_lazy[2 * node + 2] = True

            self.has_lazy[node] = False
            self.lazy_a[node] = 0
            self.lazy_d[node] = 0

    def update(self, ql, qr, a, d, node=0, l=0, r=None):
        if r is None:
            r = self.n - 1
        self.push(node, l, r)

        if r < ql or l > qr:
            return
        if ql <= l and r <= qr:
            base = (a + (l - ql) * d) % MOD
            self.lazy_a[node] = base
            self.lazy_d[node] = d
            self.has_lazy[node] = True
            self.push(node, l, r)
            return

        mid = (l + r) // 2
        self.update(ql, qr, a, d, 2 * node + 1, l, mid)
        self.update(ql, qr, a, d, 2 * node + 2, mid + 1, r)
        self.tree[node] = (self.tree[2 * node + 1] + self.tree[2 * node + 2]) % MOD

    def query(self, ql, qr, node=0, l=0, r=None):
        if r is None:
            r = self.n - 1
        self.push(node, l, r)

        if r < ql or l > qr:
            return 0
        if ql <= l and r <= qr:
            return self.tree[node]

        mid = (l + r) // 2
        left = self.query(ql, qr, 2 * node + 1, l, mid)
        right = self.query(ql, qr, 2 * node + 2, mid + 1, r)
        return (left + right) % MOD


def solve_optimized(n, A, queries):
    st = SegmentTree(A)
    total = 0

    for query in queries:
        t, l, r = query
        if t == 1:
            base = st.query(l, l)
            st.update(l, r, base, base)
        else:
            total = (total + st.query(l, r)) % MOD

    return total


n = 7
A = [1, 4, 5, 1, 6, 7, 8]
queries = [
    (1, 1, 6),
    (1, 1, 5),
    (2, 5, 5),
    (2, 3, 4),
    (2, 3, 3)
]

print(solve_optimized(n, A, queries))  # Output: 60

'''

Operation	        Complexity
Build Tree	        O(n)
Type 1 Update	    O(log n)
Type 2 Query	    O(log n)

Total	            O((n + q) × log n)

This is now fully optimized and scalable for 10⁵ queries.

'''