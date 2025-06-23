'''
Type 1 Update:

For i in range(l, r+1):
    A[i] = (i - l + 1) * A[l]

This is a position-dependent update, where:

    Each A[i] is set to (i - l + 1) * A[l]

This can't be expressed as:

    A fixed value update

    A range addition

    A constant multiplication

So, lazy propagation for range updates doesn’t directly help here.
    
What We Can Still Optimize:
    We can keep the array updates brute-force (Type 1), but use a Segment Tree for fast Type 2 (sum queries).

Plan:
    1. Build a Segment Tree over array A.

    2. For Type 1, update A as usual and call update() on the segment tree for each modified index.

    3. For Type 2, perform a range_sum() query in O(log n) time.
    
'''

MOD = 10**9 + 7

class SegmentTree:
    def __init__(self, A):
        self.n = len(A)
        self.tree = [0] * (4 * self.n)
        self.build(A, 0, 0, self.n - 1)

    def build(self, A, node, start, end):
        if start == end:
            self.tree[node] = A[start]
        else:
            mid = (start + end) // 2
            self.build(A, 2*node+1, start, mid)
            self.build(A, 2*node+2, mid+1, end)
            self.tree[node] = self.tree[2*node+1] + self.tree[2*node+2]

    def update(self, index, value, node, start, end):
        if start == end:
            self.tree[node] = value
        else:
            mid = (start + end) // 2
            if index <= mid:
                self.update(index, value, 2*node+1, start, mid)
            else:
                self.update(index, value, 2*node+2, mid+1, end)
            self.tree[node] = self.tree[2*node+1] + self.tree[2*node+2]

    def query(self, L, R, node, start, end):
        if R < start or end < L:
            return 0
        if L <= start and end <= R:
            return self.tree[node]
        mid = (start + end) // 2
        left = self.query(L, R, 2*node+1, start, mid)
        right = self.query(L, R, 2*node+2, mid+1, end)
        return left + right


def process_queries_with_segment_tree(n, A, queries):
    st = SegmentTree(A)
    total_sum = 0

    for query in queries:
        type_, l, r = query

        if type_ == 1:
            # Apply brute-force update in A
            base = A[l]
            for i in range(l, r+1):
                A[i] = (i - l + 1) * base
                st.update(i, A[i], 0, 0, n - 1)  # update segment tree

        elif type_ == 2:
            # Range sum using segment tree
            total_sum += st.query(l, r, 0, 0, n - 1)
            total_sum %= MOD

    return total_sum

n = 7
A = [1, 4, 5, 1, 6, 7, 8]
queries = [
    (1, 1, 6),
    (1, 1, 5),
    (2, 5, 5),
    (2, 3, 4),
    (2, 3, 3)
]

print(process_queries_with_segment_tree(n, A, queries))  # Output: 60

'''

Operation	        Complexity
Build Tree	        O(n)
Type 1 Update	    O(r - l + log n)
Type 2 Query	    O(log n)

Total	            O((n + q) × log n)

 So this gives you significant speed-up for Type 2 queries, while still keeping Type 1 manageable unless the range is huge.

'''

