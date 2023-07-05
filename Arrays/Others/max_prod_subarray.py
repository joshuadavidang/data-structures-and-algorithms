def max_product(nums):
    if not len(nums):
        return 0

    currMax = currMin = maxProd = nums[0]

    for i in range(1, len(nums)):
        if nums[i] < 0:
            currMax, currMin = currMin, currMax

        if nums[i] > currMax * nums[i]:
            currMax = nums[i]
        else:
            currMax *= nums[i]

        if nums[i] < currMin * nums[i]:
            currMin = nums[i]
        else:
            currMin *= nums[i]

        if currMax > maxProd:
            maxProd = currMax

    return maxProd