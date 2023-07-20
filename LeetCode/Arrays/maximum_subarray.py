def maximum_subarray(nums):
    if not nums:
        return 0

    maxSub = nums[0]
    totalSum = 0

    for num in nums:
        if totalSum < 0:
            totalSum = 0

        totalSum += num
        maxSub = max(maxSub, totalSum)

    return maxSub
