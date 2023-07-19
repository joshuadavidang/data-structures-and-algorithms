def maximum_subarray(nums):
    maxSub = nums[0]
    currSum = 0

    for num in nums:
        if currSum < 0:
            currSum = 0
        currSum += num
        maxSub = max(maxSub, currSum)

    return maxSub
