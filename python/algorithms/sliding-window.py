from math import inf


# Without sliding window technique
def max_subarray_sum_naive(nums, k):
    """
    finds the maximum sum of any concurrent subarray of size k
    """
    max_sum = -inf

    for i in range(len(nums) - k + 1):
        max_sum = max(max_sum, sum(nums[i:i+k]))

    return max_sum


# With sliding window technique
def max_subarray_sum_sliding_window(nums, k):
    """
    finds the maximum sum of any concurrent subarray of size k
    """
    max_sum = -inf
    window_sum = sum(nums[:k])

    """
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)
    OR
    """
    for i in range(len(nums) - k):
        window_sum += nums[i + k] - nums[i]
        max_sum = max(max_sum, window_sum)

    return max_sum
