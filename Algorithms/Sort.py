def sortArr(arr):
    if len(arr) == 1:
        return arr

    mid = len(arr) // 2

    left_half = sortArr(arr[:mid])
    right_half = sortArr(arr[mid:])

    return merge(left_half, right_half)


def merge(left, right):
    i = j = 0
    result = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
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


data = [5, 2, 3, 6, 12, 14, 3, 21]
assert sortArr(data) == [2, 3, 3, 5, 6, 12, 14, 21]
