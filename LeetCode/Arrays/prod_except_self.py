def productExceptSelf(nums):
    result = []

    prefix = 1
    for num in nums:
        result.append(prefix)
        prefix *= num

    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        result[i] *= postfix
        postfix *= nums[i]

    return result
