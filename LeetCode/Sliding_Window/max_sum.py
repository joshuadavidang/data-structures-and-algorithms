def max_sum(nums, k):
    if len(nums) < k:
        return -1

    maxSum = windowSum = sum(nums[:k])

    for i in range(k, len(nums)):
        windowSum = windowSum - nums[i - k] + nums[i]
        maxSum = max(maxSum, windowSum)

    return maxSum
