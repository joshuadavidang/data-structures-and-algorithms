def max_sum(nums, k):
    if len(nums) < k:
        return -1

    window_sum = sum(nums[:k])
    max_sum = 0

    for i in range(len(nums) - k):
        window_sum = window_sum - nums[i] + nums[i + k]
        max_sum = max(window_sum, max_sum)

    return max_sum
