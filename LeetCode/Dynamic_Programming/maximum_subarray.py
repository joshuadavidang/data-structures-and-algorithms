def maximum_subarray(nums):
    if len(nums) == 0:
        return 0

    totalSum = 0
    maxSum = nums[0]

    for num in nums:
        totalSum += num
        maxSum = max(maxSum, totalSum)

        if totalSum < 0:
            totalSum = 0

    return maxSum
