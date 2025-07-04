#!/usr/bin/env python3
"""
Counting Special Pairs — rewritten for clarity.

Algorithm
---------
1. Build `prefix[i]`  = #occurrences of a[i] in a[0..i].
2. Build `suffix[i]`  = #occurrences of a[i] in a[i..n‑1].
3. Sweep the array from **left to right**.
   • A Fenwick tree (BIT) keeps counts of `suffix` values that still lie to
     the *right* of the current position.
   • For every index i, we need the number of j>i with
         suffix[j] < prefix[i].
     This is `bit.query(prefix[i]‑1)`.
4. Update the BIT by *removing* the current suffix[i] (it will no longer be
   to the right on the next step).

Complexity
----------
Time  : O(n log n)  
Memory: O(n)
"""

import sys
from collections import defaultdict
from typing import List


class FenwickTree:
    """1‑based Fenwick (Binary Indexed) Tree for prefix sums."""
    def __init__(self, size: int):
        self._n = size
        self._bit = [0] * (size + 1)

    def update(self, idx: int, delta: int) -> None:
        while idx <= self._n:
            self._bit[idx] += delta
            idx += idx & -idx
        print(self._bit)

    def query(self, idx: int) -> int:
        """Sum of elements in [1 .. idx]."""
        s = 0
        while idx:
            s += self._bit[idx]
            idx -= idx & -idx
        return s


def count_special_pairs(n:int, a: List[int]) -> int:
    # prefix frequencies
    prefix = [0] * n
    freq = defaultdict(int)
    for i, x in enumerate(a):
        freq[x] += 1
        prefix[i] = freq[x]

    # suffix frequencies
    suffix = [0] * n
    freq.clear()
    for i in range(n - 1, -1, -1):
        freq[a[i]] += 1
        suffix[i] = freq[a[i]]

    print('Prefix: ', prefix)
    print('Suffix: ', suffix)
    # Fenwick tree over frequency domain (max ≤ n)
    bit = FenwickTree(n)

    # Initially insert every suffix count
    for v in suffix:
        bit.update(v, 1)
    print(" ")

    ans = 0
    for i in range(n):
        # Current element shouldn't be counted in the tree for j > i
        bit.update(suffix[i], -1)

        # How many suffix[j] < prefix[i] ?
        ans += bit.query(prefix[i] - 1)

    return ans


# Sample Input 1
n = 7
a = [1, 2, 1, 1, 2, 2, 1]
print(count_special_pairs(n, a))

# # Sample Input 2
# n = 3
# a = [1, 1, 1]
# print(count_special_pairs(n, a))

# # Sample Input 3
# n = 5
# a = [1, 2, 3, 4, 5]
# print(count_special_pairs(n, a))

    

