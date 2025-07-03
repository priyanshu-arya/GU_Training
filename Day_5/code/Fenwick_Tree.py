class FenwickTree:
    def __init__(self, size):
        self.n = size
        self.tree = [0] * (self.n + 1)

    def update(self, index, delta):
        while index <= self.n:
            self.tree[index] += delta
            index += index & -index
        print(self.tree)

    def prefix_sum(self, index):
        result = 0
        while index > 0:
            result += self.tree[index]
            index -= index & -index
            
        return result

    def range_sum(self, left, right):
        return self.prefix_sum(right) - self.prefix_sum(left - 1)

# Example usage
ft = FenwickTree(10)
ft.update(3, 5)
ft.update(5, 2)
ft.update(1, 6)
print(ft.range_sum(3, 5))  # Output: 7