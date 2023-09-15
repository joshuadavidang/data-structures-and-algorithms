# Top 50 Array Coding Problems for Interviews
# https://www.geeksforgeeks.org/top-50-array-coding-problems-for-interviews/


def reverseArr(data):
    """
    Write a program to reverse an array or string
    """

    left, right = 0, len(data) - 1
    while left < right:
        data[left], data[right] = data[right], data[left]
        left += 1
        right -= 1

    return data


arr = [1, 2, 3]
result = reverseArr(arr)
assert result == [3, 2, 1]


def sortArr(arr):
    """
    Write a program to sort the given array
    """

    if len(arr) == 1:
        return arr

    mid = len(arr) // 2

    left_half = sortArr(arr[:mid])
    right_half = sortArr(arr[mid:])

    return merge(left_half, right_half)


def merge(left, right):
    i = j = 0
    result = []

    while i < len(left) or j < len(right):
        if (j == len(right)) or (i < len(left) and left[i] < right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    return result


arr = [2, 1, 4, 3]
result = sortArr(arr)
assert result == [1, 2, 3, 4]


def sortArrayDutchAlgorithm(arr):
    """
    Sort an array of 0s, 1s and 2s | Dutch National Flag problem
    """

    low, mid, high = 0, 0, len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr


data = [0, 1, 2, 0, 1, 2]
result = sortArrayDutchAlgorithm(data)
assert result == [0, 0, 1, 1, 2, 2]


def binarySearch(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] > target:
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            return mid

    return -1


def countOccurence(arr, target):
    """
    Count number of occurrences (or frequency) in a sorted array
    """

    index = binarySearch(arr, target)
    if index == -1:
        return 0

    count = 1
    left = index - 1
    while left >= 0 and arr[left] == target:
        count += 1
        left -= 1

    right = index + 1
    while right < len(arr) and arr[right] == target:
        count += 1
        right += 1

    return count


data = [1, 1, 2, 2, 2, 2, 2, 3]
target = 2
result = countOccurence(data, target)
assert result == 5


def zigZag(arr):
    """
    Given an array of distinct elements of size N, the task is to rearrange the elements of the array in a zig-zag fashion
    so that the converted array should be in the below form:
    """

    arr.sort()

    i = 1
    while i < len(arr) - 1:
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
        i += 2

    return arr


data = [4, 3, 7, 8, 6, 2, 1]
assert zigZag(data) == [1, 3, 2, 6, 4, 8, 7]
