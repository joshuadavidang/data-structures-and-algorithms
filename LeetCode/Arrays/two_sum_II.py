def two_sum(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        currSum = nums[left] + nums[right]
        if currSum == target:
            return [left + 1, right + 1]
        elif currSum < target:
            left += 1
        else:
            right -= 1

    return None
