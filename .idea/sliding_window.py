def max_subarray_sum(nums, k):
    n = len(nums)
    if n < k:
        return None

    window_sum = sum(nums[:k])
    max_sum = window_sum

    for i in range(k, n):
        window_sum = window_sum - nums[i - k] + nums[i]
        max_sum = max(max_sum, window_sum)

    return max_sum

# Example usage
nums = [2, 1, 5, 1, 3, 2]
k = 3
result = max_subarray_sum(nums, k)
print("Maximum subarray sum:", result)  # Output should be 9