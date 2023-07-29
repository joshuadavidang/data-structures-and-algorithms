def findMaxAverage(nums, k):
    if len(nums) == 1:
        return nums[0]

    maxAvg = windowSumAvg = sum(nums[:k])

    for i in range(k, len(nums)):
        windowSumAvg = windowSumAvg - nums[i - k] + nums[i]
        maxAvg = max(maxAvg, windowSumAvg)

    return maxAvg / k
