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


def countOccurence(arr, target):
    i = binarySearch(arr, target)
    if i == -1:
        return 0

    count = 1

    left = i - 1
    while i >= 0 and arr[left] == target:
        count += 1
        left -= 1

    right = i + 1
    while right < len(arr) and arr[right] == target:
        count += 1
        right += 1

    return count


data = [1, 5, 7, 7, 7, 8, 12, 14, 21]
assert countOccurence(data, 7) == 3


def linearSearch(nums, target):
    i = 0
    while i < len(nums):
        if nums[i] == target:
            return i
        i += 1

    return -1


data = [1, 5, 7, 8, 12, 14, 21]
assert linearSearch(data, 14) == len(data) - 2
