def sortArray(nums):
    n = len(nums)
    if n == 1:
        return nums

    mid = n // 2

    left_half = sortArray(nums[:mid])
    right_half = sortArray(nums[mid:])

    return merge(left_half, right_half)


def merge(left, right):
    i = j = 0
    result = []

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result
