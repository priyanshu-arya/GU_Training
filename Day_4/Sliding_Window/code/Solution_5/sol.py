def numSubarrayProductLessThanK(nums, k):
    if k <= 1:
        return 0

    product = 1
    left = 0
    result = 0

    for right in range(len(nums)):
        product *= nums[right]

        while product >= k:
            product /= nums[left]
            left += 1

        result += (right - left + 1)

    return result
