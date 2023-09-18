def binarySearch(nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            return mid

    return -1


data = [1, 5, 7, 8, 12, 14, 21]

assert binarySearch(data, 7) == 2


def linearSearch(nums, target):
    i = 0
    while i < len(nums):
        if nums[i] == target:
            return i
        i += 1

    return -1


assert linearSearch(data, 14) == len(data) - 2
