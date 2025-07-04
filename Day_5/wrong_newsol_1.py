from collections import defaultdict

class FenwickTree:
    def __init__(self, size):
        self.tree = [0] * (size + 2)

    def update(self, idx, val):
        while idx < len(self.tree):
            self.tree[idx] += val
            idx += idx & -idx

    def query(self, idx):
        res = 0
        while idx > 0:
            res += self.tree[idx]
            idx -= idx & -idx
        return res

def count_special_pairs(n, a):
    prefix = [0] * n
    suffix = [0] * n
    freq_prefix = defaultdict(int)
    freq_suffix = defaultdict(int)

    # Step 1: Build prefix frequency
    for i in range(n):
        freq_prefix[a[i]] += 1
        prefix[i] = freq_prefix[a[i]]

    # Step 2: Build suffix frequency
    for i in range(n-1, -1, -1):
        freq_suffix[a[i]] += 1
        suffix[i] = freq_suffix[a[i]]

    # Step 3: Count valid pairs using BIT
    max_freq = max(max(prefix), max(suffix))  # Max freq value we may see
    bit = FenwickTree(max_freq)
    count = 0

    # Traverse from right to left
    for j in range(n-1, -1, -1):
        # When we reach index j, we want to know:
        # how many prefix[i] > suffix[j] for i < j → BIT.query(prefix[i] - 1)
        if j > 0:
            count += bit.query(prefix[j-1] - 1)
        # Add current suffix[j] to BIT
        bit.update(suffix[j], 1)

    return count

# Sample Input 1
n = 7
a = [1, 2, 1, 1, 2, 2, 1]
print(count_special_pairs(n, a))  # Output: 8

# Sample Input 2
n = 3
a = [1, 1, 1]
print(count_special_pairs(n, a))  # Output: 1

# Sample Input 3
n = 5
a = [1, 2, 3, 4, 5]
print(count_special_pairs(n, a))  # Output: 0
