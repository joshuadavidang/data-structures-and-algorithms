def two_sum(nums, target):
    nums_tuple = []
    for i, num in enumerate(nums):
        nums_tuple.append((num, i))

    nums_tuple.sort()
    left, right = 0, len(nums_tuple) - 1
    while left < right:
        currSum = nums_tuple[left][0] + nums_tuple[right][0]
        if currSum == target:
            return [nums_tuple[left][1], nums_tuple[right][1]]
        elif currSum < target:
            left += 1
        else:
            right -= 1
    return None
