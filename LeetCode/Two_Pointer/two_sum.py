def two_sum(nums, target):
    tuple_data = []
    for i, num in enumerate(nums):
        tuple_data.append((num, i))
    tuple_data.sort()

    left, right = 0, len(tuple_data) - 1
    while left < right:
        leftNum, leftIndex = tuple_data[left]
        rightNum, rightIndex = tuple_data[right]
        currSum = leftNum + rightNum

        if currSum == target:
            return [leftIndex, rightIndex]
        elif currSum < target:
            left += 1
        else:
            right -= 1

    return None
