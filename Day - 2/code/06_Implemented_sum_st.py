class SegmentTree:
    class Node:
        def __init__(self, start, end):
            self.start = start
            self.end = end
            self.data = 0
            self.left = None
            self.right = None

    def __init__(self, arr):
        self.root = self._construct(arr, 0, len(arr) - 1)

    def _construct(self, arr, start, end):
        if start == end:
            leaf = self.Node(start, end)
            leaf.data = arr[start]
            return leaf
        node = self.Node(start, end)
        mid = (start + end) // 2
        node.left = self._construct(arr, start, mid)
        node.right = self._construct(arr, mid + 1, end)
        node.data = node.left.data + node.right.data
        return node

    def display(self):
        self._display(self.root)

    def _display(self, node):
        if not node:
            return

        left = f"[{node.left.start}-{node.left.end}] => {node.left.data}" if node.left else "No left child"
        right = f"[{node.right.start}-{node.right.end}] => {node.right.data}" if node.right else "No right child"
        curr = f"[{node.start}-{node.end}] => {node.data}"

        print(f"{left} <= {curr} => {right}\n")
        self._display(node.left)
        self._display(node.right)

    def query(self, qsi, qei):
        return self._query(self.root, qsi, qei)

    def _query(self, node, qsi, qei):
        if node.start >= qsi and node.end <= qei:
            return node.data
        elif node.end < qsi or node.start > qei:
            return 0
        return self._query(node.left, qsi, qei) + self._query(node.right, qsi, qei)

    def update(self, index, value):
        self.root.data = self._update(self.root, index, value)

    def update_range(self, start, end, value):
        """Update all elements in the range [start, end] to a specific value."""
        for i in range(start, end + 1):
            self.root.data = self._update(self.root, i, value)

    def _update(self, node, index, value):
        if index < node.start or index > node.end:
            return node.data
        if node.start == node.end:
            node.data = value
            return node.data
        left = self._update(node.left, index, value)
        right = self._update(node.right, index, value)
        node.data = left + right
        return node.data


# Example usage
arr = [1, 3, 5, 7, 9, 11]
st = SegmentTree(arr)
st.display()

print("Query(1, 3):", st.query(1, 3))  # 15
st.update(1, 10)
print("Query(1, 3) after update:", st.query(1, 3))  # 22

st.update_range(3, 5, 20)
print("Query(1, 3) after update:", st.query(1, 3))  # 22

st.display()
