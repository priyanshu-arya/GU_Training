def maxSumGoodSubarray(A, k):
    N = len(A)
    max_sum = [0]  
    
    def backtrack(start):
        distinct = set()
        current_sum = 0
        for end in range(start, N):
            distinct.add(A[end])
            if len(distinct) > k:
                break  
            current_sum += A[end]
            max_sum[0] = max(max_sum[0], current_sum)
    
    for i in range(N):
        backtrack(i)
    
    return max_sum[0]

# Example usage:
N = 11
k = 2
A = [1, 2, 2, 3, 2, 3, 5, 1, 2, 1, 1]
print(maxSumGoodSubarray(A, k))  # Output should be 12
