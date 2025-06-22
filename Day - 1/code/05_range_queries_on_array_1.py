MOD = 10**9 + 7

def process_queries(n, A, queries):
    total_sum = 0

    for query in queries:
        type_, l, r = query

        if type_ == 1:
            # Type 1: Update A[i] from index l to r
            base = A[l]
            for i in range(l, r + 1):
                A[i] = (i - l + 1) * base

        elif type_ == 2:
            # Type 2: Sum from A[l] to A[r] and add to total_sum
            total_sum += sum(A[l:r+1])
            total_sum %= MOD

    return total_sum


# Input
n = 7
A = [1, 4, 5, 1, 6, 7, 8]
queries = [
    (1, 1, 6),
    (1, 1, 5),
    (2, 5, 5),
    (2, 3, 4),
    (2, 3, 3)
]

result = process_queries(n, A, queries)
print(result)  # Output: 60
