def binarySearch(nums, target, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return binarySearch(nums, target, mid + 1, right)
    else:
        return binarySearch(nums, target, left, mid - 1)
