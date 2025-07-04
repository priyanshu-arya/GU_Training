class FenwickTree:
    def __init__(self, size):
        self.n = size
        self.tree = [0] * (self.n + 1)

    def update(self, index, delta):
        while index <= self.n:
            self.tree[index] += delta
            index += index & -index

    def query(self, index):
        result = 0
        while index > 0:
            result += self.tree[index]
            index -= index & -index
        return result


n = 5
a = [3, 1, 4, 1, 5]

n = 5
a = [3, 3, 1, 6, 1]

# Coordinate compression
sorted_unique = sorted(set(a))
compress_map = {val: idx + 1 for idx, val in enumerate(sorted_unique)}

# Initialize Fenwick Tree
fenwick = FenwickTree(len(sorted_unique))
for i in range(1, len(sorted_unique) + 1):
    fenwick.update(i, 1)

# Calculate ranks
rank_map = {}
for val in sorted_unique:
    index = compress_map[val]
    rank_map[val] = fenwick.query(index - 1)

# Output the rank for each element in the original array
print("\n".join(str(rank_map[val]) for val in a))